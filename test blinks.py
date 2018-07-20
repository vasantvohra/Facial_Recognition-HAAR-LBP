# Import OpenCV2 for image processing
import cv2
import employee
import pickle
# Import numpy for matrices calculations
import numpy as np
import time
from pygame import mixer
from time import gmtime, strftime

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = ("haarcascade_frontalface_default.xml")
cascadePath2 = ("CustomBlinkCascade.xml")
# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);
eyeCascade=cv2.CascadeClassifier(cascadePath2)
# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX
#alert sound when recoganized and saved to file
def alert():
    mixer.init()
    alert=mixer.Sound('beep-07.wav')
    alert.play()
    time.sleep(0.1)
    alert.play()
# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
x=0
y=0
w=0
ey = 0
ex = 0
eh = 0
ew = 0
Blinks = 0
total = 2.0
blinkDetected = False
oneEyeDetected = False
blinkDetectionThreshold = 0.5
Id=()
# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:
        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (255,0,0), 4)
    # Recognize the face belongs to which ID
        Id = recognizer.predict(gray[y:y+h,x:x+w])
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = im[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(
                                roi_gray,
                                scaleFactor=1.2,
                                minNeighbors=5,
                                minSize=(15, 15),
                                maxSize=(80, 80)
                            )
        try:
             eyes
        except NameError:
             print("well, no eyes are detected!")
        else:
             ii = 0
        #eyes = eyeCascade.detectMultiScale(roi_gray)
        #for each eye in face
        for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
             if ((ii < 1 and ey < (h * .33) and (total > blinkDetectionThreshold) and oneEyeDetected == False)):
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,0,255), 2)
                print ("#########################Blink Detected##############################")
                print ('Blink Time: ', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                blinkDetected = True
                Blinks = Blinks + 1
                print("bink count",Blinks)
                alert()
                
                localtime = time.asctime( time.localtime(time.time()) )
                file = open("attendance2.txt","a")
                id1=str(Id)
                ir=id1[2]
                if (ir==','):
                    id2=id1[1]
                    file.write("\n"+id2+'                  '+localtime)
                else:
                    id2=id1[1]+id1[2]+id1[3]
                    file.write("\n"+id2+'                '+localtime)
                    print(id2)
                    print("Local current time :", localtime)
                file.close()
                cv2.putText(im, 'Blinked!', (10, 30), font, 1, (255, 0, 0), 2)
                break
	    
    #Put text describe who is in the picture
    cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
    cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3) 
    cv2.putText(im, 'Press Q to end the experiment!', (10, 460), font, 1, (255, 255, 255), 2)
    # Display the video frame with the bounded rectangle
    cv2.imshow('Blink test in Face Recognition',im) 
    
    # If 'q' is pressed, close program
    if (cv2.waitKey(10) & 0xFF == ord('q')):
        break

#alert()

#file.newlines()

#file.write("\n"+id2+'                '+localtime)
#file.write()
#file.write(localtime)

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
