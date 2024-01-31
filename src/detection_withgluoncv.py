from gluoncv import model_zoo, data, utils
import matplotlib.pyplot as plt

# Load a pre-trained YOLOv3 model
net = model_zoo.get_model('yolo3_darknet53_coco', pretrained=True)

# Load and preprocess an image
img_path = "screenshoots\\screenshot1.png"
x, img = data.transforms.presets.yolo.load_test(img_path, short=512)

# Make a prediction
class_IDs, scores, bounding_boxes = net(x)

# Visualize the image with bounding boxes and labels
ax = utils.viz.plot_bbox(img, bounding_boxes[0], scores[0],
                         class_IDs[0], class_names=net.classes)
plt.show()
