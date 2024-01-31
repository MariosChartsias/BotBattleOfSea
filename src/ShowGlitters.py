import cv2
import numpy as np

def findGlitter(frame):
    # Load the template image
    for i in range(1,7):
        template = cv2.imread(f'glitters\\glitter1_position{i}.png')  # Replace with the path to your template image

        # Load the template image
        h, w, l = template.shape

        # Convert the frame to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Initialize ORB detector
        orb = cv2.ORB_create()

        # Find the keypoints and descriptors with ORB
        kp1, des1 = orb.detectAndCompute(template, None)
        kp2, des2 = orb.detectAndCompute(frame_gray, None)

        # Create BFMatcher (Brute Force Matcher)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors
        matches = bf.match(des1, des2)

        # Sort them based on distance
        matches = sorted(matches, key = lambda x:x.distance)

        # Print the coordinates of the best match
        if len(matches) > 0:
            best_match = matches[0]
            x, y = kp2[best_match.trainIdx].pt
            print("Coordinates of glitter:")
            print((int(x), int(y)))


def findColor(frame, target_color):
    # Convert the frame from RGB to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # Define a range of acceptable colors in HSV
    lower_bound = np.array(target_color - np.array([10, 50, 50]))
    upper_bound = np.array(target_color + np.array([10, 50, 50]))

    # Create a mask using inRange
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours
    for contour in contours:
        # Get the centroid of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            print("Coordinates of target color:")
            print((cx, cy))
            # Optionally, draw a circle at the centroid
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    return frame