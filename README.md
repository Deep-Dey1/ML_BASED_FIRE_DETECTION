# ML_BASED_FIRE_DETECTION
Real-Time Fire Detection System Using Raspberry Pi and Machine Learning
Overview:

This project aims to develop an intelligent fire detection system leveraging machine learning and IoT technology to identify and alert users in case of fire. The system is designed to detect fire through a trained machine learning model and, upon detection, send real-time alerts to users via SMS. To enhance accuracy, a verification mechanism is implemented to allow users to visually confirm alerts.

Project Steps:

Model Training:

The machine learning model for fire detection was trained using a YOLOv8n model, utilizing Google Colab for computational resources and Kaggle’s public fire dataset.
Model training included 200 epochs to optimize accuracy, and Ultralyitcs YOLOv8 was used for high performance and precision.
Throughout the training process, various metrics such as Precision-Recall (PR) curves, F1 scores, and confusion matrices were generated, along with a results.csv file.
After successful training, the model was saved as best.pt, which was further compressed to a plain text format for easier deployment on a Raspberry Pi.
Implementation on Raspberry Pi:

A Raspberry Pi 4 Model B is the primary device used for implementing the fire detection system. To capture video input, I connected my mobile camera to the Raspberry Pi using DroidCam and API-based communication.
The trained best.pt model is utilized in a Python script (main.py) to analyze real-time camera input for fire detection.
Real-Time Alerts:

Upon detecting a fire, the system triggers Twilio's API to send an SMS alert to the user’s mobile number.
To ensure accuracy, a web-based confirmation mechanism is integrated. Given the possibility of false positives from the model, users can verify alerts by checking a live feed.
Verification via Web Platform:

A basic website, hosted on Replit, displays the live camera feed allowing users to visually inspect the detected "fire" alert.
The site is built using HTML, CSS, and JavaScript and is protected by Firebase authentication to ensure secure access.
Along with the SMS alert, the website link is provided to users, enabling them to verify if an actual fire is present, reducing unnecessary concerns from false alarms.
Additional Circuit Integration:

A physical circuit with a breadboard, buzzer, and LED lights is connected to the Raspberry Pi.
When fire is detected, the system triggers the buzzer to beep, and the LEDs blink to provide a visual and auditory warning on-site.
System Trigger with Push Button:

To facilitate easy testing and reset, a button.py script is implemented.
The script is linked to a push button connected to the Raspberry Pi, and pressing it triggers the main.py script, initiating the fire detection process manually as needed.
Conclusion:

This fire detection project combines machine learning, IoT, and real-time alerting to offer a robust solution for monitoring and responding to fire hazards. The integration of a verification platform reduces the impact of false alerts, enhancing reliability, and the use of Raspberry Pi with connected hardware provides an affordable and accessible setup. This system can be adapted for various environments where immediate fire detection and confirmation are critical.
