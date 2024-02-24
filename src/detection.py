import cv2
import numpy as np
import pyautogui  # Import pyautogui for screen capture
from ultralytics import YOLO
from ultralytics.utils.plotting import colors, Annotator
from PIL import ImageGrab
from win32api import GetSystemMetrics
import Tools as tl
import keyboard #pip install keyboard
import time
from Paths import *




model = YOLO(relative_path_object_model_1640px_windows)
modelOCR=YOLO(relative_path_ocr_model_400px_windows)
names = model.model.names

text=''
confirm=False
enable_to_click_glitter=True
click_next_glitter=True
navigation=False
height, width = GetSystemMetrics(0), GetSystemMetrics(1)
# Set the center point for the visioneye annotation
center_point = (-10, pyautogui.size()[1])  # Use the screen height as the y-coordinate

run=True
i=1
while run:

    img = ImageGrab.grab(bbox=(0,0, width, height))
    img_np = np.array(img)
    screen_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # Predict objects in the screenshot using the YOLO model
    results = model.predict(screen_bgr, conf=0.2)
    boxes = results[0].boxes.xyxy.cpu()
    clss = results[0].boxes.cls.cpu().tolist()
    Dictionary = results[0].names


    #prediction for Navigation
    resultsNavigation = model.predict(screen_bgr , imgsz=360, conf=0.2)
    boxesNavigation = results[0].boxes.xyxy.cpu()
    clssNavigation = results[0].boxes.cls.cpu().tolist()
    DictionaryNavigation = results[0].names



    #print(Dictionary.items())
    # Annotate the screenshot with bounding boxes and class labels
    annotator = Annotator(screen_bgr, line_width=2)
    for box, cls in zip(boxes, clss):
        #print(f"box={box}")
        #print(f"cls={cls}->{Dictionary[cls]}")
        print(f"**************detection********************box={box[0]}, cls={cls}->{Dictionary[cls]}")   

        if(cls==12.0): #12: ocrText
            #print(f'box[0]={box[0]},box[1]={box[1]},box[2]={box[2]},box[3]={box[3]}')
            Numbers=tl.screenshot_array(box[0],box[1],box[2],box[3],i)
            text=tl.getText(Numbers)
            i=i+1
            print(f'text={text} and object={Dictionary[cls]}')
        ##################################################################        OCR CAPTURE CODE       ###########################################################################
        if(cls==5.0 and text!=''): #5.0: TextFieldToBotQuestion
            tl.click(box[0],box[2],box[1],box[3])   
            time.sleep(1) 
            pyautogui.typewrite(text)
            time.sleep(1)
            text=''
            print(f'text={text}')
            confirm=True
            #run = False   
        if(cls==4.0 and confirm): #4.0: ConfirmToBotQuestion
            confirm=False
            tl.click(box[0],box[2],box[1],box[3])
        #############################################################################################################################################################################
        if(cls==9.0): #9.0: glitterClicked
            tl.centerCamera()
            time.sleep(2) 
            break
        elif(cls==8.0): #8.0: glitter
            tl.stableCam()
            tl.click(box[0],box[2],box[1],box[3])
            tl.mouse_in_safe_zone()
            


        
                
            

        annotator.box_label(box, label=names[int(cls)], color=colors(int(cls)))
        annotator.visioneye(box, center_point)

    if keyboard.is_pressed('esc'):
            print("Stop Loop!")
            run = False

# Close all OpenCV windows
cv2.destroyAllWindows()
