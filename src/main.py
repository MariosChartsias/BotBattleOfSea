import keyboard
import cv2
import numpy as np
import pyautogui  
from ultralytics import YOLO
from win32api import GetSystemMetrics
import time
from Paths import *
import os
import shutil
import random

from utils.get_os_paths import *

global screen_bgr 
global last_execution_time

time_of_pause=0
DEBUG = False

def screenshot_array(x1, y1, x2, y2,i):
    """ Convert screenshot picture of OCR to numpy array
    """
    # Convert coordinates to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    # Expand the region by 5 pixels
    x1 -= 5
    y1 -= 5
    x2 += 5
    y2 += 5

    # Take a screenshot of the expanded region
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    screenshot.save(get_app_path(f'OcrTexts\\OCRtext{i}.png'))
    if DEBUG:
        print("function: screenshot_array")  # for debugging only
    time.sleep(time_of_pause)  # for debugging only
    return np.array(screenshot)


#this absolute path works only for ipynb and not for the actual Tools.py file
def getText(screenshot_array_format,modelOCR=YOLO(absolute_path_ocr_model_640px_windows)):
    """ It receives screenshot numpy array and generates the coresponding CAPTCHA sollution
    """
    results = modelOCR.predict(screenshot_array_format,imgsz=640, conf=0.2)
    boxes = results[0].boxes.xyxy.cpu()
    clss = results[0].boxes.cls.cpu().tolist()
    Dictionary = results[0].names
    mapping = {}
    for box, cls in zip(boxes, clss):
        mapping[box[0]] = Dictionary[cls][-1]
        #print(f"box={box[0]}, cls={cls}->{Dictionary[cls]}")
    
    sorted_dict = {k: v for k, v in sorted(mapping.items(), key=lambda item: item[0])}
    string=''
    for value in sorted_dict.values():
        string=string+value

    if DEBUG:
        print("function: getText")
        time.sleep(time_of_pause) 
    return string

def mouse_in_safe_zone():
    """ Safe region is a spot where the mouse is resting to prevent overlapping with other elements
    """
    pyautogui.FAILSAFE = False  # Disables the fail-safe feature
    pyautogui.moveTo(0, 0, duration=0)

    if DEBUG:
        print("function: mouse_in_safe_zone") # for debugging only
        time.sleep(time_of_pause) # for debugging only

def stableCam():
    """ Clicks W and S button to stop the centering focus on ship
        TODO: This should be configured from the user to any key
    """
    pyautogui.typewrite('ws')
    if DEBUG:
        print("function: stableCam") # for debugging only
        time.sleep(time_of_pause) # for debugging only

def centerCamera():
    """ It focuses the camera to center of the game by pressign the G key
        TODO: The control KEY should be configured by the user (or click on the center feature)
    """
    pyautogui.typewrite('g')
    if DEBUG:
        print("function: centerCamera")
        time.sleep(time_of_pause) # for debugging only


def handleOCRtext(objects, final_array, ocr_counter):
    """ Once it detects the OCR text --> 
        1. Get screenshot
        2. Solve CAPTCHA
        3. Click on cell and complete the sollution
        4. Click on Confirm button
        5. Return True: screenshot counter increment
    """
    label_18_OCRText = objects[objects[:, 5] == 18] # 18 -> OCRText
    
    if DEBUG:
        print(label_18_OCRText)

    if len(label_18_OCRText) > 0:
        ocr_screenshot = screenshot_array(label_18_OCRText[0][0], label_18_OCRText[0][1], label_18_OCRText[0][2], label_18_OCRText[0][3], ocr_counter)
        Numbers = getText(ocr_screenshot)
        if len(Numbers) == 4:
            # TODO: Use Dictionary and not hardcoded integers
            label_7_OCRText = final_array[final_array[:, 3] == 7] # 7: 'TextFieldToBotQuestion'
            label_4_OCRText = final_array[final_array[:, 3] == 4] # 4: 'TextFieldToBotQuestion'
            if(len(label_7_OCRText) > 0 and len(label_4_OCRText) > 0):
                pyautogui.click(label_7_OCRText[0][0], label_7_OCRText[0][1])
                time.sleep(random.randint(1, 3))
                pyautogui.typewrite(Numbers)
                time.sleep(random.randint(1, 3))
                pyautogui.click(label_4_OCRText[0][0], label_4_OCRText[0][1])
                return True
    return False

def delete_folder(folder_path):
    """
    Check if the folder exists and delete it if it does.

    Args:
    - folder_path (str): The path to the folder to be checked and deleted.
    
    Returns:
    - bool: True if the folder was deleted successfully or didn't exist, False otherwise.
    """
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            if DEBUG:
                print(f"The folder '{folder_path}' has been deleted.")
            return True
        except Exception as e:
            #print(f"Error deleting the folder '{folder_path}': {e}")
            return False
    else:
        #print(f"The folder '{folder_path}' does not exist.")ws
        return True  # Return True because the folder doesn't exist, no action required


# This is not working runs only created in project parent directory
folder_path = get_app_path("last_detection/")

def moveTo_z_points(x_left, y_top, x_right, y_bottom, point_code=None):
    """ Clicks on the corners of the map
    """
    if point_code is None:
        point_code = random.randint(1, 4)

    if point_code == 1:
        # Top-left point
        pyautogui.moveTo(x_left, y_top)
    elif point_code == 2:
        # Top-right point
        pyautogui.moveTo(x_right, y_top)
    elif point_code == 3:
        # Bottom-left point
        pyautogui.moveTo(x_left, y_bottom)
    elif point_code == 4:
        # Bottom-right point
        pyautogui.moveTo(x_right, y_bottom)

    pyautogui.mouseDown()
    pyautogui.mouseUp()

def check_navigation_eligibility(label_17_map, order):
    """ Checks the map to navigate in the next spot if only last execution time has passed 30 seconds
    """
    global last_execution_time
    current_time = time.time()
    if current_time - last_execution_time >= 30:
        last_execution_time = current_time
        if len(label_17_map) > 0:
            x_left, y_top = label_17_map[0][0] + 10, label_17_map[0][1] + 10
            x_right, y_bottom = label_17_map[0][2] - 10, label_17_map[0][3] - 10
            moveTo_z_points(x_left, y_top, x_right, y_bottom)
            time.sleep(1)
            pyautogui.click((order[1], order[2]))

def getScreenshot():
    """ Get the WHOLE screen capture
    """
    img = pyautogui.screenshot()
    img_np = np.array(img)
    screen_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    return screen_bgr


def getTimeSleep(distance_in_pixels):
    """ Calculates the seconds that the boat will need to catch a glitter + safety time 2 secs
    """
    if(distance_in_pixels!=None and distance_in_pixels!=0):
        x=distance_in_pixels
        u=72 #pixels/second
        t=x/u
        if(t==float('inf')): return 0
        else: return max(0,t)



def predict(folder_path_to_read, model=YOLO(absolute_path_object_model_2000px_windows)):
    """ Based on the trained model --> detect and return the objects
        #!!must conf=0.15: Accuracy of the model

        TODO: model2 with imgsz=600 to detect only the window area in order to constrain the click area
    """
    delete_folder(folder_path)
    results = model(folder_path_to_read, save_dir = folder_path, stream=True , conf=0.15, retina_masks=True , save=True, save_txt=False, imgsz=2000)  
    for result in results:
        boxes = result.boxes.cpu().numpy().data # Boxes object for bounding box outputs
        Dictionary=result.names

        if DEBUG:
            print(f"--->{Dictionary}")
            print(f"results--->{result}")
    
        return boxes, Dictionary
    

def getCenterOfBoxes(ObjectArray):
    ""
    #print(ObjectArray)
    center_x = (ObjectArray[:, 0] + ObjectArray[:, 2]) / 2
    center_y = (ObjectArray[:, 1] + ObjectArray[:, 3]) / 2
    ObjectArray = np.column_stack((center_x, center_y, ObjectArray[:, 5])) # objects[:, 5] is the class of objects 
    row_of_myship = ObjectArray[ObjectArray[:, 2] == 6] #6 is the label of myShip
    
    if(len(row_of_myship)!=0):
        x_ship = row_of_myship[0][0]
        y_ship = row_of_myship[0][1]
    else:
        x_ship=float('inf')
        y_ship=float('inf')

    distances = np.linalg.norm(np.column_stack((ObjectArray[:,0], ObjectArray[:,1])) - np.column_stack((x_ship, y_ship)), axis=1)
    ObjectArray = np.column_stack((center_x, center_y, distances, objects[:, 5]))

    return ObjectArray


def sort_array_by_column(array, column_index):
    """
    Sorts the given array based on the values in the specified column.

    Parameters:
    array (numpy.ndarray): The input array to be sorted.
    column_index (int): The index of the column based on which the sorting should be performed.

    Returns:
    numpy.ndarray: The sorted array.
    """
    # Check if the column index is valid
    if column_index < 0 or column_index >= array.shape[1]:
        raise ValueError("Column index is out of bounds.")

    # Sort the array by the values in the specified column
    sorted_indices = np.argsort(array[:, column_index])
    sorted_array = array[sorted_indices]

    return sorted_array

def reverse_dict(input_dict):
    """
    """
    return {value: key for key, value in input_dict.items()}

def nearest_glitter_or_random_glitter(final_array_sorted, object_dict):
    """ Checks if there is any glitter on the scene else gives the navigation coordinates (offseted coordinates from corner)
    """
    object_dict = reverse_dict(object_dict)
    # Accessing the labels directly from the object_dict using their names
    label_14_glitters = final_array_sorted[final_array_sorted[:, 3] == object_dict['glitter']] #14 -> glitter
    label_15_glitter_clicked = final_array_sorted[final_array_sorted[:, 3] == object_dict['glitterClicked']] #15 -> the label of glitter clicked
    label_03_stableCam = final_array_sorted[final_array_sorted[:, 3] == object_dict['CenterMyBoat']] #3 -> CenterMyBoat
    label_19_pointOfMoving = final_array_sorted[final_array_sorted[:, 3] == object_dict['pointOfMoving']] #19 -> pointOfMoving
    label_06_myShip = final_array_sorted[final_array_sorted[:, 3] == object_dict['MyShip']] #6 -> MyShip
    label_17_map = final_array_sorted[final_array_sorted[:, 3] == object_dict['map']] #17 -> map
    
    isGlitter = len(label_14_glitters)>0
    isGlitterClicked = len(label_15_glitter_clicked)>0
    isCameraMoving = len(label_03_stableCam)==0
    isBoatMoving = len(label_19_pointOfMoving)>0
    isPOVonScreen = len(label_06_myShip)>0
    isMapAvailable =  len(label_17_map)>0
    
    if DEBUG:
        print(f"case1:({isGlitter} or {isGlitterClicked}) and {isCameraMoving}")
        print(f"case2:({not isGlitter} and {not isCameraMoving})")

    if(isGlitter or isGlitterClicked) and isCameraMoving: #this will stable the camera and retake screenshot
        stableCam()  
        return None
    elif(not isGlitter and not isCameraMoving):
        centerCamera()
    elif(not isGlitter and not isGlitterClicked and isBoatMoving and isPOVonScreen):
        global last_execution_time
        last_execution_time = time.time()-30
    elif(not isGlitter and not isGlitterClicked):
        if time.time() - last_execution_time >= 30:
            stableCam()

        
    if(isGlitterClicked):
        time.sleep(4) #this is the time of waiting until the clicked glitter dissappears
        return None
    
    elif isGlitter: # Check if there are any glitters 
        x=label_14_glitters[0][0]
        y=label_14_glitters[0][1]
        distance = label_14_glitters[0][2]
        return 'glitterToClick',x,y,distance
    elif not isGlitter and not isCameraMoving:
        x=label_03_stableCam[0][0]
        y=label_03_stableCam[0][1]-50
        return 'navigation',x,y
   
    return None


run = True
pyautogui.FAILSAFE = False #to move the mouse in corner (0,0)
last_execution_time = time.time()-30
ocr_counter=1


while run:
    
    start_time = time.time()
    objects, objects_dict= predict(getScreenshot())
    end_time = time.time()
    print(f"Execution time before optimization: {end_time - start_time} seconds")
    
    if DEBUG:
        print(objects)
   
    if objects.size!=0:
        
        final_array = getCenterOfBoxes(objects)
        #print(final_array)
        if(handleOCRtext(objects, final_array, ocr_counter)):
            ocr_counter=ocr_counter+1

        sorted_array = sort_array_by_column(final_array,2) #2nd column is the column of distances

        if DEBUG:
            print(sorted_array)
        order = nearest_glitter_or_random_glitter(sorted_array, objects_dict)
        
        if DEBUG:
            print(order) #None if there is no Ship /
        if(order is not None and order[0]=='glitterToClick'):
            pyautogui.click((order[1],order[2]))
            pyautogui.moveTo(0, 0, duration=0)
            last_execution_time = time.time()-30
            time.sleep(getTimeSleep(order[3]))
        elif(order is not None and order[0]=='navigation'):
            navigation_trigger=True
            isShipOnScreen = len(final_array[final_array[:, 3] == 6])>0 #6 -> MyShip
            isPOVonScreen = len(final_array[final_array[:, 3] == 19])>0 #19 -> pointOfMoving 
            if(isShipOnScreen and isPOVonScreen):   
                 last_execution_time = time.time()-30
            label_17_map = objects[objects[:, 5] == 17] # 17 -> map
            check_navigation_eligibility(label_17_map, order)
            

    if keyboard.is_pressed('esc'):
            print("Stop Loop!")
            run = False

