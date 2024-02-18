import pyautogui
import numpy as np
from ultralytics import YOLO

def click(x1, x2, y1, y2):
    middle_x = (x1 + x2) / 2
    middle_y = (y1 + y2) / 2
    pyautogui.click(middle_x, middle_y)

def screenshot(x1, y1, x2, y2,i):
    # Convert coordinates to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))

    # Save the screenshot
    screenshot.save(f'OcrTexts\screenshot{i}.png')

def screenshot_array(x1, y1, x2, y2,i):
    # Convert coordinates to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))
    screenshot.save(f'OcrTexts\screenshot{i}.png')

    return (np.array(screenshot))

def getText(screenshot_array_format,modelOCR=YOLO("yolov8_ocr.pt")):
    results = modelOCR.predict(screenshot_array_format,imgsz=300, conf=0.2)
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

    return string

def mouse_in_safe_zone():
    pyautogui.FAILSAFE = False  # Disables the fail-safe feature
    pyautogui.moveTo(0, 0, duration=0)

import random

def getWidth_Height(x1, x2, y1, y2):
    # Ensure x1 < x2 and y1 < y2
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    
    Width=x_max-x_min
    Height=y_max-y_min
    
    return Width, Height

def getMiddle_point(x1, x2, y1, y2):
    middle_x = (x1 + x2) / 2
    middle_y = (y1 + y2) / 2
    
    return(middle_x, middle_y)

def stableCam():
    pyautogui.typewrite('ws')