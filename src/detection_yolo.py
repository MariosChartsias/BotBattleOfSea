import torch
from torchvision import models, transforms
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Load the pre-trained SSD model
model = models.detection.ssd300(pretrained=True)
model.eval()

# Load and preprocess an image
image_path = "AreYouABot\\3546.png"
image = Image.open(image_path)

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
    prediction = model(image_tensor)

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
