# Import OpenCV2 for image processing
import cv2
import employee
import pickle
#Import numpy for matrices calculations
import numpy as np
import time
from pygame import mixer

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = ("haarcascade_frontalface_default.xml")
cascadePath2 = ("haarcascade_eye.xml")
# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);
eyeCascade = cv2.CascadeClassifier(cascadePath2)
# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX


# alert sound when recoganized and saved to file
def alert():
    mixer.init()
    alert = mixer.Sound('beep-07.wav')
    alert.play()
    time.sleep(0.1)
    alert.play()

#SAVE to file
def attendance(Id, lt):
    file = open("attendance4.txt", "a")
    id1 = str(Id)
    ir = id1[2]
    ir2 = id1[3]
    if (ir == ','):
        id2 = id1[1]
        print("EMPLOYEE ID:", id2)
        print("Local current time :", lt)
        file.write("\n" + id2 + '                  ' + lt)
        alert()
        print("ALERT!!    ATTENDANCE MARKED")
    elif (ir2 == ','):
        id2 = id1[1]+id1[2]
        print("EMPLOYEE ID:", id2)
        print("Local current time :", lt)
        file.write("\n" + id2 + '                  ' + lt)
        alert()
        print("ALERT!!    ATTENDANCE MARKED") 
    else:
        id2 = id1[1] + id1[2] + id1[3]
        file.write("\n" + id2 + '                ' + lt)
        print("EMPLOYEE ID:", id2)
        print("Local current time :", lt)
        alert()
        print("ALERT!!    ATTENDANCE MARKED")
    file.close()


# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
eyeDetected = False
oneEyeDetected = False
x = 0
y = 0
w = 0
Id = ()
# Loop
while True:
    # Read the video frame
    ret, im = cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    # For each face in faces
    for (x, y, w, h) in faces:
        # Create rectangle around the face
        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 4)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = im[y:y + h, x:x + w]
        # Recognize the face belongs to which ID
        Id = recognizer.predict(gray[y:y + h, x:x + w])  
        cv2.putText(im, 'Face Detected', (10, 30), font, 1, (255, 0, 0), 2)
        ip=Id[0]
        # to detect eye in face 
        eyes = eyeCascade.detectMultiScale(roi_gray,
               scaleFactor = 1.2,
                             minNeighbors = 5,
                                            minSize = (15, 15),
                                                      maxSize = (80, 80))

        try:
            eyes
        except NameError:
            print("No eyes detected!")
        else:
            ii = 0
        # for each eye in face
        for (ex, ey, ew, eh) in eyes:
            if ((ip >= 1 and ii < 1 and ey < (h * .33) and oneEyeDetected == False and eyeDetected == False)):
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                cv2.putText(im, 'Eye Detected!', (10, 30), font, 1, (255, 0, 0), 2)
                # local time on pc
                lt = time.asctime(time.localtime(time.time()))
                attendance(Id,lt) 
                id5=Id
                #time.sleep(200)
                if id5==Id:
                    #attendance marked
                     eyeDetected = True
                else:
                     #attendance not marked
                     eyeDetected = False
        # Put text describe who is in the picture
    cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
    cv2.putText(im, str(Id), (x, y - 40), font, 2, (255, 255, 255), 3)
    cv2.putText(im, 'Press Q to end the Attendance!', (10, 460), font, 1, (255, 255, 255), 2)

    # Display the video frame with the bounded rectangle
    cv2.imshow('AAPNA Attendance Monitoring System',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
