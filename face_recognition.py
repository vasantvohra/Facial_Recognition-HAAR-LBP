# Import OpenCV2 for image processing
import cv2
import employee
import pickle
# Import numpy for matrices calculations
import numpy as np
import time
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = ("haarcascade_frontalface_default.xml")

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
x=0
y=0
w=0
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
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id = recognizer.predict(gray[y:y+h,x:x+w])
        # Check the ID if exist 
        #for i in Id:
            # search the database for id and gives name/other details
            #employee.search(i)
            #print(i)
           #if(i==int()):
            #   d=i[0]
             #  Id=(d)
            #elif(i==2):
             #   Id="2"

        #if not exist, then it is Unknown
            #else:
                #Id="not in database"
	    
	    #Put text describe who is in the picture
    cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
    cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('Face Recognition',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)
# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
