import cv2
# from cv2 import cv2
img= cv2.VideoCapture(0,cv2.CAP_DSHOW)
#img = cv2.resize(img, (500,500))
while True:
    faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    getCoordinates=faceCascade.detectMultiScale(image=img,scaleFactor=1.1,minNeighbors=4)

    for (x,y,w,h) in getCoordinates:
        cv2.rectangle(img, pt1=(x,y), pt2=(x+w,y+h), color=(0,0,255),thickness=2)

    cv2.imshow("myImage",img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(0)

#cv2.destroyAllWindows()

