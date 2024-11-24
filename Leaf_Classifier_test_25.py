import cv2
import numpy as np
from cvzone.ClassificationModule import Classifier
import math

# Initialize camera and classifier
cap = cv2.VideoCapture(0)
classifier = Classifier("Model2/keras_model.h5", "Model2/labels.txt")

# Parameters
imgSize = 300
labels = ["Hibiscus leaf", "Guava leaf"]  # Updated labels
confidence_threshold = 0.5

# Expanded HSV color range for both lighter and darker green leaves
lower_green = np.array([25, 30, 20])  # Lower range adjusted for darker green shades
upper_green = np.array([85, 255, 255])

while True:
    success, img = cap.read()
    if not success:
        break

    imgOutput = img.copy()

    # Convert to HSV color space for better leaf isolation
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply morphological operations to remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours of the leaf in the masked area
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Assume the largest contour is the leaf
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Crop and resize the leaf region
        imgCrop = img[y:y + h, x:x + w]

        # Check if the cropped image has valid size to resize
        if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            aspectRatio = h / w
            if aspectRatio > 1:  # Tall image
                scale = imgSize / h
                newWidth = math.ceil(scale * w)
                imgResize = cv2.resize(imgCrop, (newWidth, imgSize))
                wGap = math.ceil((imgSize - newWidth) / 2)
                imgWhite[:, wGap:newWidth + wGap] = imgResize
            else:  # Wide image
                scale = imgSize / w
                newHeight = math.ceil(scale * h)
                imgResize = cv2.resize(imgCrop, (imgSize, newHeight))
                hGap = math.ceil((imgSize - newHeight) / 2)
                imgWhite[hGap:newHeight + hGap, :] = imgResize

            # Perform leaf classification
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            confidence_value = prediction[index]

            if confidence_value >= confidence_threshold:
                label = labels[index]
                cv2.putText(imgOutput, f"{label} ({confidence_value * 100:.1f}%)",
                            (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                cv2.rectangle(imgOutput, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the output
    cv2.imshow("Leaf Detection", imgOutput)
    key = cv2.waitKey(1)

    if key == 27:  # Press "Esc" to exit
        break

cap.release()
cv2.destroyAllWindows()
