# FaceDetection_HaarCascade
Using openCV and Haar Cascade classifier to detect faces
-----------------------------------------------------------------------

 ## Dependencies (libraries)
  * openCV
  * numpy
  
 ## Environment
  * Windows 10
  * Anaconda 3
  * Python 3.6
 
 ## Execute   
   python face_detection.py
 
 ## Accuracy
 1. You can try another XML file to test accuracy: 
  
     haarcascade_frontalface_default.xml
  
 2. You can modify the parameters in faceCascade.detectMultiScale like:
            
     scaleFactor=1.1,
     
     minNeighbors=3,
     
     minSize=(30, 30)
 
