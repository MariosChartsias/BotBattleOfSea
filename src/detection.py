import torch
from torchvision import models, transforms
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import pyautogui
import numpy as np

class ObjectDetectorFromString:
    def __init__(self, frame_path):
        self.frame = frame_path

        # Load the pre-trained Faster R-CNN model
        self.model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
        self.model.eval()

        # Load and preprocess an image
        image = Image.open(self.frame)

        # Ensure the image has 3 channels (RGB)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Apply torchvision transforms
        preprocess = transforms.Compose([
            transforms.ToTensor(),
        ])

        image_tensor = preprocess(image).unsqueeze(0)

        # Make a prediction
        with torch.no_grad():
            prediction = self.model(image_tensor)

        # Print the predicted bounding boxes and labels
        # print(prediction)

        # Visualize the image with bounding boxes and labels
        image_with_boxes = image.copy()
        draw = ImageDraw.Draw(image_with_boxes)

        # Get the predicted boxes, labels, and scores
        boxes = prediction[0]['boxes'].cpu().numpy()
        labels = prediction[0]['labels'].cpu().numpy()
        scores = prediction[0]['scores'].cpu().numpy()

        # Draw bounding boxes and labels on the image
        for box, label, score in zip(boxes, labels, scores):
            draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline="red", width=2)
            draw.text((box[0], box[1]), f"{int(label)}: {score:.2f}", fill="red")

        # Display the image with bounding boxes and labels
        plt.imshow(image_with_boxes)
        plt.axis('off')
        plt.show()

# Example usage:
#detector = ObjectDetectorFromString("screenshots\\screenshot21.png")


class ObjectDetector:
    def __init__(self, frame):
        # If the input is a PyAutoGUI screenshot, convert it to a NumPy array
        if isinstance(frame, pyautogui.screenshot().__class__):
            frame = np.array(frame)

        self.frame = frame

        # Load the pre-trained Faster R-CNN model
        self.model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
        self.model.eval()

        # Convert the NumPy array to a PIL Image
        image = Image.fromarray(self.frame)

        # Ensure the image has 3 channels (RGB)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Apply torchvision transforms
        preprocess = transforms.Compose([
            transforms.ToTensor(),
        ])

        image_tensor = preprocess(image).unsqueeze(0)

        # Make a prediction
        with torch.no_grad():
            prediction = self.model(image_tensor)

        # Print the predicted bounding boxes and labels
        # print(prediction)

        # Visualize the image with bounding boxes and labels
        self.image_with_boxes = image.copy()
        self.draw = ImageDraw.Draw(self.image_with_boxes)

        # Get the predicted boxes, labels, and scores
        self.boxes = prediction[0]['boxes'].cpu().numpy()
        self.labels = prediction[0]['labels'].cpu().numpy()
        self.scores = prediction[0]['scores'].cpu().numpy()

    def getPlot(self):
        # Draw bounding boxes and labels on the image
        for box, label, score in zip(self.boxes, self.labels, self.scores):
            #self.draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline="red", width=2)
            self.draw.text((box[0], box[1]), f"{int(label)}: {score:.2f}", fill="red")

        # Display the image with bounding boxes and labels
        plt.imshow(self.image_with_boxes)
        plt.axis('off')
        plt.show()


    def get_object_coordinates(self, target_label=8):
        """
        Get the coordinates (x, y) of the bounding box for the specified object label.

        Parameters:
        - target_label (int): The label of the object to find (default is 8).

        Returns:
        - tuple or None: Coordinates (x, y) if the object is found, None otherwise.
        """
        # Find the index of the target label in the labels array
        target_index = np.where(self.labels == target_label)[0]

        if len(target_index) > 0:
            # Get the bounding box coordinates for the first instance of the target label
            target_box = self.boxes[target_index[0]]
            x, y = target_box[0], target_box[1]
            return x, y
        else:
            print(f"Object with label {target_label} not found.")
            return None



# Example usage:
screenshot = pyautogui.screenshot()
detector = ObjectDetector(screenshot)
detector.getPlot()


