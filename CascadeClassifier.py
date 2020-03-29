import cv2


cap=cv2.VideoCapture(0)

cas=cv2.CascadeClassifier("haarcascade_eye.xml")
while(True):

    # Capture frame-by-fram""e
    ret, frame = cap.read()
    #cv2.imshow("color",frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray", gray)
    set=cas.detectMultiScale(gray)
    # Display the resulting frame
    for x,y,w,h in set:
        frame=cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)
    cv2.imshow("preview",frame)
    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()
