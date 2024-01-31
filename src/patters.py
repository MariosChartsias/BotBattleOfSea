import cv2
import numpy as np
from PIL import Image

# Create the main array
main_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create the subarray you want to find
sub_array = np.array([[5, 2], [8, 9]])

# Find the indices where the subarray matches in the main array
indices = np.isin(main_array, sub_array)


image = cv2.imread('screenshoots\\screenshot1.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image2 = cv2.imread('screenshoots\\screenshot1_result.png')
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


indices = np.isin(gray_image, gray_image2)
# Convert the boolean array to an integer array (True -> 0, False -> 255)
#integer_array = np.where(indices, 0, 255).astype(np.uint8)


# Create an image from the integer array
#image = Image.fromarray(integer_array)

# Save or display the image
#image.save('screenshot1_result.png')
#image.show()


nonzero_indices = np.nonzero(gray_image2)

length = len(nonzero_indices)
print(f'max value={int((max(nonzero_indices[0])+min(nonzero_indices[0]))/2)}')

x=int((max(nonzero_indices[0])+min(nonzero_indices[0]))/2)
y=int((max(nonzero_indices[1])+min(nonzero_indices[1]))/2)
print(x,y)