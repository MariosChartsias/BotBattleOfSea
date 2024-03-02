import sys

import keyboard
# sys.path.append('..\..\src') # this ensures that the src models are located to import them bellow
#sys.path.append('C:\\Users\\Marios\\Desktop\\Μάριος\\BotBattleOfSea\\src') deprecated absolute path
import cv2
import numpy as np
import pyautogui  # Import pyautogui for screen capture
import ultralytics
from ultralytics import YOLO
from ultralytics.utils.plotting import colors, Annotator
from PIL import ImageGrab
from win32api import GetSystemMetrics
#import keyboard #pip install keyboard
import time
from Paths import *
import math
import os
import shutil
import random

from utils.get_os_paths import *

time_of_pause=0

def click(middle_x,middle_y):
    pyautogui.click(middle_x, middle_y)
    print("function: click") # for debugging only
    time.sleep(time_of_pause) # for debugging only


def screenshot(x1, y1, x2, y2,i):
    # Convert coordinates to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))

    # Save the screenshot
    screenshot.save(get_app_path(f"OcrTexts/screenshot{i}.png"))
    print("function: screenshot") # for debugging only
    time.sleep(time_of_pause) # for debugging only

def screenshot_array(x1, y1, x2, y2,i):
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

    print("function: screenshot_array")  # for debugging only
    time.sleep(time_of_pause)  # for debugging only
    return np.array(screenshot)


#this absolute path works only for ipynb and not for the actual Tools.py file
def getText(screenshot_array_format,modelOCR=YOLO(absolute_path_ocr_model_640px_windows)):
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

    print("function: getText") # for debugging only
    time.sleep(time_of_pause) # for debugging only
    return string

def mouse_in_safe_zone():
    pyautogui.FAILSAFE = False  # Disables the fail-safe feature
    pyautogui.moveTo(0, 0, duration=0)
    print("function: mouse_in_safe_zone") # for debugging only
    time.sleep(time_of_pause) # for debugging only

import random

def getWidth_Height(x1, x2, y1, y2):
    # Ensure x1 < x2 and y1 < y2
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    
    Width=x_max-x_min
    Height=y_max-y_min

    print("function: getWidth_Height") # for debugging only
    time.sleep(time_of_pause) # for debugging only
    return Width, Height

def getMiddle_point(x1, x2, y1, y2):
    middle_x = (x1 + x2) / 2
    middle_y = (y1 + y2) / 2
    
    print("function: getMiddle_point") # for debugging only
    time.sleep(time_of_pause) # for debugging only
    return(middle_x, middle_y)

def stableCam():
    pyautogui.typewrite('ws')
    print("function: stableCam") # for debugging only
    time.sleep(time_of_pause) # for debugging only

def centerCamera(): # g is default letter for centering the cammera 
    pyautogui.typewrite('g')
    print("function: centerCamera") # for debugging only
    time.sleep(time_of_pause) # for debugging only

def cartesian_distance(x1, y1, x2, y2):
    """
    Calculate the Cartesian distance between two points (x1, y1) and (x2, y2).

    Args:
    - x1, y1 (float): Coordinates of the first point.
    - x2, y2 (float): Coordinates of the second point.

    Returns:
    - float: The Cartesian distance between the two points.
    """
    print(np.array([x2, y2]).shape, np.array([x1, y1]).shape)
    distance = np.linalg.norm(np.array([x2, y2]) - np.array([x1, y1]))
    return distance

def handleOCRtext(objects, final_array, ocr_counter):
    #print(objects)
    label_18_OCRText = objects[objects[:, 5] == 18] # 18 -> OCRText
    print(label_18_OCRText)
    if len(label_18_OCRText) > 0:
        ocr_screenshot = screenshot_array(label_18_OCRText[0][0], label_18_OCRText[0][1], label_18_OCRText[0][2], label_18_OCRText[0][3], ocr_counter)
        Numbers = getText(ocr_screenshot)
        if len(Numbers) == 4:
            label_7_OCRText = final_array[final_array[:, 3] == 7] # 7: 'TextFieldToBotQuestion'
            label_4_OCRText = final_array[final_array[:, 3] == 4] # 4: 'TextFieldToBotQuestion'
            if(len(label_7_OCRText) > 0 and len(label_4_OCRText) > 0):
                click(label_7_OCRText[0][0], label_7_OCRText[0][1])
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
            print(f"The folder '{folder_path}' has been deleted.")
            return True
        except Exception as e:
            #print(f"Error deleting the folder '{folder_path}': {e}")
            return False
    else:
        #print(f"The folder '{folder_path}' does not exist.")ws
        return True  # Return True because the folder doesn't exist, no action required



# Example usage:
folder_path = get_app_path("last_detection/")
# delete_folder(folder_path)

def moveTo_z_points(x_left, y_top, x_right, y_bottom, point_code=None):
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
    img = pyautogui.screenshot()
    img_np = np.array(img)
    screen_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    return screen_bgr


def getTimeSleep(distance_in_pixels):
    if(distance_in_pixels!=None and distance_in_pixels!=0):
        x=distance_in_pixels
        u=72 #pixels/second
        t=x/u
        if(t==float('inf')): return 0
        else: return max(0,t)

global screen_bgr 
global last_execution_time

def predict(folder_path_to_read, model=YOLO(absolute_path_object_model_2000px_windows)):
    #folder_path_to_read = r'C:\Users\Marios\Desktop\Μάριος\BotBattleOfSea\src\ObjectDetections'
    delete_folder(folder_path)
    results = model(folder_path_to_read, save_dir = folder_path, stream=True , conf=0.15, retina_masks=True , save=True, save_txt=False, imgsz=2000)  # returns Results objects #!!must conf=0.15
    for result in results:
        boxes = result.boxes.cpu().numpy().data # Boxes object for bounding box outputs
        Dictionary=result.names
        print(f"--->{Dictionary}")
        return boxes
    

def getCenterOfBoxes(ObjectArray):
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


#sort array function:
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

def nearest_glitter_or_random_glitter(final_array_sorted):
    label_14_glitters = final_array_sorted[final_array_sorted[:, 3] == 14] #14 -> glitter
    print(label_14_glitters)
    label_15_glitter_clicked = final_array_sorted[final_array_sorted[:, 3] == 15] #15 -> the label of glitter clicked
    label_03_stableCam = final_array_sorted[final_array_sorted[:, 3] == 3] #3: -> the label of CenterMyBoat 
    label_19_pointOfMoving = final_array_sorted[final_array_sorted[:, 3] == 19] #19 -> pointOfMoving 
    label_06_myShip = final_array_sorted[final_array_sorted[:, 3] == 6] #6 -> MyShip
    label_17_map = final_array_sorted[final_array_sorted[:, 3] == 17] # 17 -> map
    
    isGlitter = len(label_14_glitters)>0
    isGlitterClicked = len(label_15_glitter_clicked)>0
    isCameraMoving = len(label_03_stableCam)==0
    isBoatMoving = len(label_19_pointOfMoving)>0
    isPOVonScreen = len(label_06_myShip)>0
    isMapAvailable =  len(label_17_map)>0
    
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
    #navigation--------
    

    return None


# objects= predict(get_app_path("ObjectDetections")) #this is only for debugging purposes


# final_array = getCenterOfBoxes(objects)

# if(handleOCRtext(objects, final_array, ocr_counter)):
#     ocr_counter=ocr_counter+1

# sorted_array = sort_array_by_column(final_array,2) #2nd column is the column of distances

# order = nearest_glitter_or_random_glitter(sorted_array)
# if(order is not None and order[0]=='glitterToClick'):
#     pyautogui.moveTo((order[1],order[2]))g
#     print(order) #None if there is no Ship / x and y if exist both / x and y if only glitter exist

run = True
pyautogui.FAILSAFE = False #to move the mouse in corner (0,0)
last_execution_time = time.time()-30
ocr_counter=1


while run:
    
    objects= predict(getScreenshot())
   
    if objects.size!=0:
        
        final_array = getCenterOfBoxes(objects)
        #print(final_array)
        if(handleOCRtext(objects, final_array, ocr_counter)):
            ocr_counter=ocr_counter+1

        sorted_array = sort_array_by_column(final_array,2) #2nd column is the column of distances

        print(sorted_array)
        order = nearest_glitter_or_random_glitter(sorted_array)
        

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

