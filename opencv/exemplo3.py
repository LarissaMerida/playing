import numpy as np
import cv2 as cv

face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

print("Qual a imagem?")
img = input()
image = cv.imread(img)
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face.detectMultiScale(image_gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow('imagem', image)
cv.waitKey(0)
cv.destroyAllWindows()
