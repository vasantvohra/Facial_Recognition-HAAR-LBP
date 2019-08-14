# Attendance Monitoring System
### Simple Attendance Monitoring System Internship Project.

[Slide Show/PPT](https://www.slideshare.net/slideshow/embed_code/key/eDxtfA7muM7PYQ)
#### Working: 
![Image](https://github.com/vasantvohra/Facial_Recognition-HAAR-LBP/blob/master/mermaid%20working.PNG)

|       Features | Implementation |Scripts
|----------------|-----------|-----------------------------|
|Employee Database| File Processing System |[Employee-detail.py](https://github.com/vasantvohra/Facial_Recognition-HAAR-LBP/blob/master/employee_detail.py)|
|Face Capture | **OpenCV**, Captures the 10 faces and stores in dataset folder   | [newface.py](https://github.com/vasantvohra/Facial_Recognition-HAAR-LBP/blob/master/newface.py)
| Features Extraction| **LBP** Recognizer extract FaceFeatures store it with ID into YML file    |[Training.py](https://github.com/vasantvohra/Facial_Recognition-HAAR-LBP/blob/master/training.py)          |
|Face Recognizer| predicts against the YML file using LBP|[face_recognition.py](https://github.com/vasantvohra/Facial_Recognition-HAAR-LBP/blob/master/face_recognition.py)|

| Additional | Description | 
|-------------|------------|
| Text to Speech  | Pyttsx3 for greetings |
| Alert | Py Game used,  Playsound could be used
| Date Time | Date Time module|
| Eye blink | Liveliness Detection eyeHaarCascade
## Setup
```python
 - clone this repo
 - git clone https://github.com/vasantvohra/Facial_Recognition-HAAR-LBP.git
 - pip install -r requirements.txt
 - Execute the menu.py
 - follow the steps
	 1. Enter Employee database
	 2. let your face get captured
	 3. Training happens automatically
	 4. run the face_recognizer.py on raspberry pi at deployed area
```
### Next Steps
- Upload CSV file directly to google sheets
- Automatically build individual employee attendance report
- Further data analysis on attendance reports

#### Demo
![Image](https://github.com/vasantvohra/Facial_Recognition-HAAR-LBP/blob/master/image.png)
