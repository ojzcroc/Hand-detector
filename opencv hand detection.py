import sys
sys.path.append('/home/ojzcroc/Downloads/nxt-python-2.2.2/')
import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
from subprocess import Popen, PIPE
fore = 0
back = 0
left = 0
right = 0
uparrow = '''keydown Up
keyup Up
'''
downarrow = '''keydown Down
keyup Down
'''
def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)
while( cap.isOpened() ) :
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
  
    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(img.shape,np.uint8)

    max_area=0
   
    for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
                cx = int(moments['m10']/moments['m00']) # cx = M10/M00
                cy = int(moments['m01']/moments['m00']) # cy = M01/M00
              
    centr=(cx,cy)
    cv2.circle(img,centr,5,[0,0,255],2)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)
          
    cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    hull = cv2.convexHull(cnt,returnPoints = False)
    
    if(1):
               defects = cv2.convexityDefects(cnt,hull)
               mind=0
               maxd=0
               for i in range(defects.shape[0]):
                    s,e,f,d = defects[i,0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    dist = cv2.pointPolygonTest(cnt,centr,True)
		    if dist >= 130:
			print "forward"
			fore += 1
			keypress(uparrow)
			back = 0
		    elif dist <= 30:
			if dist >= -20:
			    print "back"
			    back += 1
			    fore = 0
			    keypress(downarrow)
		    if int(end[0]) <= 70:
			print "right"
			right += 1
			left = 0
		    elif int(end[0]) >= 400:
			print "left"
			left += 1
			right = 0
                    cv2.line(img,start,end,[0,255,0],2)
                    cv2.circle(img,far,5,[0,0,255],-1)
               i=0
    cv2.imshow('output',drawing)
    cv2.imshow('input',img)
                
    k = cv2.waitKey(10)
    if k == 27:
        break
