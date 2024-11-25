<div align="center">
  <img src="Leafid12.jpg" alt="LEAFID" width="40%">
</div>

# LeafID: ML-Based Leaf Identification System  

**LeafID** is a robust and interactive system designed to classify leaves in real-time using a pre-trained machine learning model. It provides accurate identification of leaf types while supporting live webcam feed processing and PDF report generation.

---

## 🚀 Project Overview  

- **Frontend**: Built with Gradio for an intuitive user interface, enabling users to upload images for classification.  
- **Backend**: Implements OpenCV for image processing, integrates a pre-trained model from Teachable Machine, and supports real-time detection using a webcam feed.  
- **Dataset**: Utilizes a licensed dataset trained on Teachable Machine for Hibiscus and Guava leaf classification.  

---

## 🌟 Key Features

- **Real-Time Detection**: Seamlessly detects and analyzes leaves using a live webcam feed or uploaded images.  
- **AI-Driven Classification**: Powered by a pre-trained model developed with **Teachable Machine**.  
- **Detailed Reporting**: Automatically generates downloadable PDF reports for each classification.  
- **Optimized Leaf Detection**: Tailored HSV color filtering ensures accurate leaf isolation, even in varying lighting conditions.
  
---

## 🔍 Workflow  

### **1. Data Collection and Model Training**
- Gathered images of Hibiscus and Guava leaves.
- Collected them in the folders and applied augmentation.
- Trained a custom ML model using **Google's Teachable Machine** to classify the two types of leaves.
- Exported the trained model in TensorFlow Lite format (`keras_model.h5`) with labels (`labels.txt`).

### **2. Backend Image Processing**
- Initialized a webcam feed using OpenCV for real-time leaf detection.
- Processed the image frames to isolate leaves based on their green color using HSV color masking.
- Detected the largest contour in the processed mask to identify the leaf region.
- Resized the detected leaf to a standard dimension (300x300 pixels) for model compatibility.

### **3. Classification with Pre-Trained Model**
- Integrated the Teachable Machine model for classification using the `cvzone.ClassificationModule`.
- Used a confidence threshold of 50% to filter predictions.
- Labeled the detected leaf as **Hibiscus leaf** or **Guava leaf** with the confidence percentage.

### **4. User Interaction and Output**
- Provided a **Gradio Interface** for image uploads, classification, and PDF report generation.
- Displayed real-time classification results with bounding boxes and labels using the webcam feed.
- Generated detailed PDF reports summarizing the classification results.

---



