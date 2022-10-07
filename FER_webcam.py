from fer import FER
import cv2
import time
vid = cv2.VideoCapture(1)
start_time = time.time()


face_cascade = cv2.CascadeClassifier('C:/Users/Elif/Desktop/Emotion Recognition/4th week/haarcascade_frontalface_default.xml')
while(True):
      
    ret, frame = vid.read()
    

    if time.time() - start_time >= 3 and ret!=False:

        detector = FER()
        emotion, score = detector.top_emotion(frame) # 'happy', 0.99  = detector.detect_emotions(frame)
  
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        txt = str(emotion) + " " + str(score)
        cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        cv2.imshow("frames",frame)
        start_time = time.time()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()