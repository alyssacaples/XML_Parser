import xml.etree.ElementTree as ET
import numpy as np
import cv2
import matplotlib.pyplot as plt
import ast

tree = ET.parse('annotations.xml')
root = tree.getroot()

def parse_line(line):
    individ = line.split(';')
    xy = []
    for each in individ:
        xy.append(np.array(each.split(','), dtype=np.float32))
        # point = []
        # for y in each.split(','):
        #     point.append(np.float64(y))
        # xy.append(np.array(point))

    return np.array(xy)

f1_label = []
f2_label = []
f3_label = []
f4_label = []

for child in root.iter('polyline'):
    child_points = parse_line(child.attrib['points']) # this is a string
    
    if(child.attrib['label'] == 'f1'):
        f1_label.append(child_points)
        #print("f1")
    elif(child.attrib['label'] == 'f2'):
        f2_label.append(child_points)
        #print("f2")
    elif(child.attrib['label'] == 'f3'):
        f3_label.append(child_points)
        #print("f3")
    elif(child.attrib['label'] == 'f4'):
        f4_label.append(child_points)
        #np.concatenate((f4_label, child_points), axis=0)
        #print("f4")

#vect = np.vectorize(np.float)
f1_label = np.array(f1_label, dtype=object)
f2_label = np.array(f2_label, dtype=object)
f3_label = np.array(f3_label, dtype=object)
f4_label = np.array(f4_label, dtype=object)





#print(np.shape(f4_label))

img = cv2.imread('Snap_Speed3_0_0.jpg')

for shape in f1_label:

    cv2.fillPoly(img, np.int32([shape]), color=(255, 0, 0))

for shape in f2_label:

    cv2.fillPoly(img, np.int32([shape]), color=(255, 255, 0))

for shape in f3_label:

    cv2.fillPoly(img, np.int32([shape]), color=(0, 255, 0))

for shape in f4_label:

    cv2.fillPoly(img, np.int32([shape]), color=(255, 0, 255))

#points = np.array([[160, 130], [350, 130], [250, 300]])

# cv2.fillPoly(img, f1_label, color=(255, 0, 0))

# cv2.fillPoly(img, np.int32([f2_label]), color=(255, 255, 0))

# cv2.fillPoly(img, np.int32([f3_label]), color=(0, 255, 0))

# cv2.fillPoly(img, np.int32([f4_label]), color=(255, 0, 255))

cv2.imshow("filled polygon", img)

#wait for the user to press any key to 
#exit window
cv2.waitKey(0)
  
#Closing all open windows
cv2.destroyAllWindows()

filename = 'anno_img.jpg'

cv2.imwrite(filename, img)

