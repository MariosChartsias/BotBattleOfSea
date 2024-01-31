import cv2 as cv
import sys

class ImageDisplayer:
    def __init__(self, path):
        self.path = path

    def showImage(self):
        img = cv.imread(cv.samples.findFile(self.path))
        if img is None:
            sys.exit("Could not read the image.")
        cv.imshow("Display window", img)
        k = cv.waitKey(0)
        if k == ord("c"):
            cv.imwrite("output_image.jpg", img)  # Provide a filename for saving the image

