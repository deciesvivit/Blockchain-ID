#from typing import final
import easyocr
import cv2
import numpy as np
import pandas as pd
import os
import sys
import subprocess
from PIL import Image
import pyperclip


image = str(sys.argv[1])
#print('Enter your name')
#name = input()
img = cv2.imread(image)

#print(image)
#print('Type 1 for passport , 2 for aadhar , 3 for PAN , 4 for DL and 5 for any other ID')
#opt=input()
path = 'faces'

#if opt==2 or opt==4:
#    reader = easyocr.Reader(['en','hi'])
#else:
#    reader = easyocr.Reader(['en'])

#result = reader.readtext(img , detail=0)

#namel = name.lower()
#check = namel in (string.lower() for string in result)

#if(check):
#    pass
#else:
#    print('Please upload a clearer image')
#    exit()
# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
#for (x, y, w, h) in faces:
#    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = img[y:y + h, x:x + w] 
    
    cv2.imwrite(os.path.join(path , 'face' + str(w) + str(h) + '_faces.jpg'), roi_color)
    imc = Image.open(r'faces/face' + str(w) + str(h) + '_faces.jpg')
    print('Is this a clear image of your face? (y/n)')
    imc.show()
    con=input()
    if con=='y':
        imgpath=str('face' + str(w) + str(h) + '_faces.jpg')
        break

#df = pd.DataFrame (result, columns = ['Details Found'])
#print(df)
#with open(r'output.txt', 'w') as fp:
#    for item in result:
#        
#        fp.write("%s\n" % item)

#pathn = r'output.txt'
#print('Confirm your details and type any key to confirm after saving the file')
#subprocess.Popen(['notepad.exe', pathn])
#conf=input()
#imgpa = 'faces/' + imgpath
#with open('output.txt', 'r') as file:
#    data = file.read().rstrip()
#pyperclip.copy(data)