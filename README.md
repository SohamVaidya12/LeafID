<div style="background-color: #e8f5e9; padding: 30px; border-radius: 10px;">

  <div align="center">
    <img src="Leafid12.jpg" alt="LEAFID" width="40%">
  </div>

  <div style="background-color: #f1f8e9; padding: 20px; border-radius: 8px;">

    <h1>LeafID: ML-Based Leaf Identification System</h1>

    <p><strong>LeafID</strong> is a robust and interactive system designed to classify leaves in real-time using a pre-trained machine learning model. It provides accurate identification of leaf types while supporting live webcam feed processing and PDF report generation.</p>

    <hr>

    <h2>🚀 Project Overview</h2>

    <ul>
      <li><strong>Frontend</strong>: Built with Gradio for an intuitive user interface, enabling users to upload images for classification.</li>
      <li><strong>Backend</strong>: Implements OpenCV for image processing, integrates a pre-trained model from Teachable Machine, and supports real-time detection using a webcam feed.</li>
      <li><strong>Dataset</strong>: Utilizes a licensed dataset trained on Teachable Machine for Hibiscus and Guava leaf classification.</li>
    </ul>

    <hr>

    <h2>🌟 Key Features</h2>

    <ul>
      <li><strong>Real-Time Detection</strong>: Seamlessly detects and analyzes leaves using a live webcam feed or uploaded images.</li>
      <li><strong>AI-Driven Classification</strong>: Powered by a pre-trained model developed with <strong>Teachable Machine</strong>.</li>
      <li><strong>Detailed Reporting</strong>: Automatically generates downloadable PDF reports for each classification.</li>
      <li><strong>Optimized Leaf Detection</strong>: Tailored HSV color filtering ensures accurate leaf isolation, even in varying lighting conditions.</li>
    </ul>

    <hr>

    <h2>🔍 Workflow</h2>

    <h3>1. Data Collection and Model Training</h3>
    <ul>
      <li>Gathered images of Hibiscus and Guava leaves.</li>
      <li>Collected them in the folders and applied augmentation.</li>
      <li>Trained a custom ML model using <strong>Google's Teachable Machine</strong> to classify the two types of leaves.</li>
      <li>Exported the trained model in TensorFlow Lite format (<code>keras_model.h5</code>) with labels (<code>labels.txt</code>).</li>
    </ul>

    <h3>2. Backend Image Processing</h3>
    <ul>
      <li>Initialized a webcam feed using OpenCV for real-time leaf detection.</li>
      <li>Processed the image frames to isolate leaves based on their green color using HSV color masking.</li>
      <li>Detected the largest contour in the processed mask to identify the leaf region.</li>
      <li>Resized the detected leaf to a standard dimension (300x300 pixels) for model compatibility.</li>
    </ul>

    <h3>3. Classification with Pre-Trained Model</h3>
    <ul>
      <li>Integrated the Teachable Machine model for classification using the <code>cvzone.ClassificationModule</code>.</li>
      <li>Used a confidence threshold of 50% to filter predictions.</li>
      <li>Labeled the detected leaf as <strong>Hibiscus leaf</strong> or <strong>Guava leaf</strong> with the confidence percentage.</li>
    </ul>

    <h3>4. User Interaction and Output</h3>
    <ul>
      <li>Provided a <strong>Gradio Interface</strong> for image uploads, classification, and PDF report generation.</li>
      <li>Displayed real-time classification results with bounding boxes and labels using the webcam feed.</li>
      <li>Generated detailed PDF reports summarizing the classification results.</li>
    </ul>

    <hr>

    <h2>Backend Overview</h2>

    <p>The backend of the "LeafID" system utilizes a pretrained machine learning model for real-time classification of leaf types using a webcam. It focuses on identifying <strong>Hibiscus</strong> and <strong>Guava</strong> leaves.</p>

    <h3>Key Features:</h3>
    <ul>
      <li><strong>Leaf Detection</strong>: Uses OpenCV to capture and process the webcam feed.</li>
      <li><strong>Contour Detection</strong>: Isolates the largest contour, assumed to be the leaf.</li>
      <li><strong>Pretrained Model</strong>: Trained with <strong>Teachable Machine</strong> for Hibiscus and Guava leaf classification.</li>
      <li><strong>Real-Time Prediction</strong>: Displays the classified leaf type with a confidence score.</li>
    </ul>

    <h3>Process:</h3>
    <ul>
      <li>Capture the webcam feed.</li>
      <li>Process and isolate the leaf using color filtering and contour detection.</li>
      <li>Classify the leaf using the pretrained model.</li>
      <li>Display the classification result on the video feed.</li>
    </ul>

    <h3>Libraries and Tools Used:</h3>
    <ul>
      <li><strong>OpenCV</strong> for image processing.</li>
      <li><strong>cvzone</strong> for model classification.</li>
      <li><strong>Teachable Machine</strong> for the custom model.</li>
    </ul>

    <h3>Interactive Video Demonstration:</h3>
    <p>Click the button below to watch the backend in action:</p>
    <a href="PlantID.mp4" target="_blank">
      <button style="background-color:#FF6347; color:white; padding:15px 32px; text-align:center; font-size:16px; border:none; cursor:pointer; border-radius:8px; margin: 10px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
        🎥 Watch the Backend in Action
      </button>
    </a>

    <p>Alternatively, you can view the video directly below:</p>

    <video width="100%" controls>
      <source src="PlantID.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>

</div>


 











