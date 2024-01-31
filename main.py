from src.ShowIMG import ImageDisplayer
from src.ShowGlitters import findGlitter,findColor


#image_displayer = ImageDisplayer("AreYouABot\\2644.png")
#image_displayer.showImage()


import cv2
import pyautogui
import numpy as np

# Get the screen resolution
screen_width, screen_height = pyautogui.size()

# Set the video writer
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("screen_capture.avi", fourcc, 20.0, (screen_width, screen_height))

while True:
    # Capture the screen using pyautogui
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array
    frame = np.array(screenshot)

    # Convert BGR to RGB (OpenCV uses BGR)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    #output.write(frame)

    cv2.namedWindow("Screen Capture", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Screen Capture", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # Display the frame
    cv2.imshow("Screen Capture", frame)

    # Call the function to find glitter and print coordinates
    #findGlitter(frame)
     # Call the function to find color and print coordinates
    target_color = np.array([220, 178, 93])  # Adjust the target color as needed (BGR format)
    frame_with_color = findColor(frame, target_color)

    # Break the loop if the 'Esc' key is pressed
    if cv2.waitKey(100) == 27:  # 27 is the ASCII code for the 'Esc' key
        break
    cv2.destroyWindow("Screen Capture")
    cv2.waitKey(200)
        

# Close all OpenCV windows after the loop
cv2.destroyAllWindows()

# Release the video writer
output.release()

