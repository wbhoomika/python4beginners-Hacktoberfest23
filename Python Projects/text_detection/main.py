import cv2
import numpy as np

# Load the EAST text detection model
net = cv2.dnn.readNet("frozen_east_text_detection.pb")

# Load the image
image = cv2.imread("your_image.jpg")
original_image = image.copy()
(H, W) = image.shape[:2]

# Define the output layers' names
layerNames = [
    "feature_fusion/Conv_7/Sigmoid",
    "feature_fusion/concat_3"
]

# Prepare the image for text detection
blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)

# Forward pass through the network to get the text regions
net.setInput(blob)
(scores, geometry) = net.forward(layerNames)

# Find the bounding boxes of text regions
rectangles = []
confidences = []

for y in range(0, scores.shape[2]):
    scores_data = scores[0, 0, y, 0]
    xData0 = geometry[0, 0, y, 0]
    xData1 = geometry[0, 0, y, 1]
    xData2 = geometry[0, 0, y, 2]
    xData3 = geometry[0, 0, y, 3]
    angles = geometry[0, 0, y, 4]

    for x in range(0, scores.shape[3]):
        if scores_data[x] < 0.5:
            continue

        (offsetX, offsetY) = (x * 4.0, y * 4.0)

        angle = angles[x]
        cos = np.cos(angle)
        sin = np.sin(angle)

        h = xData0[x] + xData2[x]
        w = xData1[x] + xData3[x]

        endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
        endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
        startX = int(endX - w)
        startY = int(endY - h)

        rectangles.append((startX, startY, endX, endY))
        confidences.append(scores_data[x])

# Apply non-maximum suppression to remove overlapping bounding boxes
boxes = cv2.dnn.NMSBoxes(rectangles, confidences, 0.5, 0.3)

# Loop over the remaining boxes and draw them on the image
for i in boxes:
    i = i[0]
    (startX, startY, endX, endY) = rectangles[i]
    cv2.rectangle(original_image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# Display the result
cv2.imshow("Text Detection", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
