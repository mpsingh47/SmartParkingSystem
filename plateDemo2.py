import cv2
import pytesseract as pyt
import numpy as np

import demoForm

class main:
    def __init__(self,fname):
        img = cv2.imread(fname)
        img = cv2.resize(img,(400,390))
        pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        plateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
        print(plateCascade)

        getCoordinates = plateCascade.detectMultiScale(image=img, scaleFactor=1.1, minNeighbors=4)

        for (x,y,w,h) in getCoordinates:
            a,b = (int(0.02*img.shape[0]),int(0.025*img.shape[1]))
            plate = img[y:y+h, x:x+w]
            kernal = np.ones((1,1), np.uint8)
            plate = cv2.dilate(src=plate, kernel=kernal, iterations=1)
            plate = cv2.erode(src=plate, kernel=kernal, iterations=1)

            plateGray = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
            (thresh,plate) = cv2.threshold(plateGray,100,25,cv2.THRESH_BINARY_INV)

            text = pyt.image_to_string(plate)
            text = ''.join(e for e in text if e.isalnum())
            print(text)
            # cv2.imwrite(filename='newPlate.png',img=plate)
            cv2.rectangle(img=img,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2)
            cv2.putText(img,text,(x,y+10),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,255),3)

        # cv2.imshow('Image',plate)
        cv2.imshow('Image',img)
        demoForm.main(text)
        cv2.waitKey(0)
    

# main("carnumberplate1.png")