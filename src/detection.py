import cv2
import numpy as np
import pyautogui  # Import pyautogui for screen capture
from ultralytics import YOLO
from ultralytics.utils.plotting import colors, Annotator
import Tools as tl
import keyboard #pip install keyboard
import time




model = YOLO("yolov8_1640.pt")
modelOCR=YOLO("yolov8_ocr.pt")
names = model.model.names

text=''
confirm=False
enable_to_click_glitter=True
click_next_glitter=True
navigation=False

# Set the center point for the visioneye annotation
center_point = (-10, pyautogui.size()[1])  # Use the screen height as the y-coordinate

run=True
i=1
while run:

    

    # Capture a screenshot of the screen
    screen = np.array(pyautogui.screenshot())

    # Convert the screenshot to BGR format (OpenCV uses BGR by default)
    screen_bgr = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    # Predict objects in the screenshot using the YOLO model
    results = model.predict(screen_bgr)
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
        if(cls==8.0): #8.0: glitter
            tl.stableCam()
            tl.click(box[0],box[2],box[1],box[3])
            time.sleep(9)
            break
        else:
            if(cls==3.0): #3.0: CenterMyBoat
                tl.click(box[0],box[2],box[1],box[3])
            for boxNav, clsNav in zip(boxesNavigation, clssNavigation):
                print(f"**************detection********************boxNav={boxNav[0]}, clsNav={clsNav}->{DictionaryNavigation[clsNav]}")   
                if(clsNav==8.0):
                    glitterNav=True
                    break
                else:
                    glitterNav=False 
                    if(clsNav==3.0): #3.0: CenterMyBoat
                        tl.click(box[0],box[2],box[1],box[3])  

                if(clsNav==2.0 and not glitterNav): #2:0 BattleOfSeaWindow
                    Width,Height = tl.getWidth_Height(boxNav[0],boxNav[2],boxNav[1],boxNav[3])
                    x,y=tl.getMiddle_point(boxNav[0],boxNav[2],boxNav[1],boxNav[3])
                    print(f'Width={Width} and Height={Height}')
                    pyautogui.click(Width-x, Height-y)
                    time.sleep(8)
                
            

        annotator.box_label(box, label=names[int(cls)], color=colors(int(cls)))
        annotator.visioneye(box, center_point)

    if keyboard.is_pressed('esc'):
            print("Stop Loop!")
            run = False

# Close all OpenCV windows
cv2.destroyAllWindows()
