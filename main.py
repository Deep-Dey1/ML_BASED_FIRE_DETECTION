from ultralytics import YOLO
import cvzone
import cv2
import math
from twilio.rest import Client
import os
import RPi.GPIO as GPIO
import time

# GPIO setup for the buzzer
BUZZER_PIN = 26
LED_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to beep the buzzer
def beep_buzzer(duration=0.5):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    time.sleep(duration)
# Function to blink LEDs
def Blink_LED(duration=0.5):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    time.sleep(duration)
# Function to send SMS
def send_sms():
    account_sid = 'your twilio account sid'
    auth_token = 'your twilio account auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Fire has been detected by the Fire Detector.\nPlease visit the link to see the camera input: https://93a5f42f-4cd8-4af1-a340-de5d953ef393-00-1f2kpikqrt09p.pike.replit.dev/',
        from_='your assigned virtual number from twilio',
        to='reciever mobile number'  # Replace with the actual recipient's number
    )

    print(f"SMS sent successfully. SID: {message.sid}")

# Check if model file exists
if not os.path.exists('best.pt'):
    print("Model file not found!")
    exit()

# Replace with your Android camera's IP stream
camera_ip = 'input feed ip of your mobile camera'  # Replace with your phone's IP

# Open video capture stream from camera
cap = cv2.VideoCapture(camera_ip)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

model = YOLO('best.pt')

# Reading the classes
classnames = ['fire']
sms_sent = False

# Set lower resolution to improve performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_count = 0
frame_skip = 3  # Process every 3rd frame

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame or end of video.")
            break

        # Skip frames to improve processing time
        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        result = model(frame, stream=True)

        # Getting bbox, confidence, and class names information to work with
        for info in result:
            boxes = info.boxes
            for box in boxes:
                confidence = box.conf[0]
                confidence = math.ceil(confidence * 100)
                Class = int(box.cls[0])
                if confidence > 50:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                    cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                       scale=1.5, thickness=2)

                    # Send SMS and beep buzzer if fire detected and SMS not already sent
                    if not sms_sent:
                        print("Fire detected. Sending SMS and beeping buzzer...")
                        send_sms()
                        var1 = 4
                        while(var1 > 0):
                            beep_buzzer()  # Buzzer beeps when fire is detected
                            Blink_LED() # Blinks LEDS when fire detected 
                        sms_sent = True

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()  # Ensure GPIO resources are released
