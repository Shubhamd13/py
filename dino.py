import numpy as np
import cv2
import pyautogui as pgi
from mss import mss
from PIL import ImageGrab

#mon = {'top': 160, 'left': 160, 'width': 200, 'height': 200}

sct = mss()
while 1:
    sct=ImageGrab.grab()
    #x,y=pgi.position()
    r,g,b=sct.getpixel((525,375))
    if(r==83 and g==83 and b==83):
        print("jump")
        pgi.hotkey('space')
