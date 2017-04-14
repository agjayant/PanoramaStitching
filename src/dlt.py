
# coding: utf-8

# In[ ]:

import numpy as np
import argparse
import cv2
import math
from sympy import Matrix

def dlt(image, p1, p2 ):

    # image = cv2.imread('../images/note.png')

    ###---------------- note.png
    # p1  = [(73,239), (356,117), (475,265), (187,443)]
    # p2  = [(73,239), (365,239), (365,450), (73,450)]

    # image = cv2.imread('../images/house.jpg')

    ##----------------- house.jpg --- res1
    # p1  = [(138,208), (138,100), (180,106), (180,205)]
    # p2  = [(138,208), (138,100), (195,100), (195,205)]

    ##----------------- house.jpg --- res2
    # p1  = [(100,180), (100,95), (208,180), (208,115)]
    # p2  = [(100,180), (100,95), (215,95), (215,180)]

    # image = cv2.imread('../images/roadsign.jpg')

    ###----------------- roadsign.jpg --- res1
    # p1  = [(119,207), (119,267), (380,164), (380,227)]
    # p2  = [(119,207), (119,267),(400,207), (400,267)]

    ###----------------- roadsign.jpg --- res2
    # p1  = [(105,60), (105,120), (377,126), (377,186)]
    # p2  = [(105,60), (105,120), (390,60), (390,120)]

    # image = cv2.imread('../images/house2.jpg')

    ##----------------- house2.jpg --- res1
    # p1  = [(490,340), (605,338), (490,487), (603,468)]
    # p2  = [(490,340),(645,340), (490,487), (645,487)]

    ##----------------- house2.jpg --- res2
    # p1  = [(310,205), (310,477), (119,274), (119,410)]
    # p2  = [(310,205), (310,477), (45,205), (45,477)]

    # cv2.circle(image, p1[0], 1, 1555, thickness=5, lineType=8, shift=0)
    # cv2.circle(image, p2[0], 1, 25, thickness=5, lineType=8, shift=0)

    # cv2.circle(image, p1[1], 1, 1555, thickness=5, lineType=8, shift=0)
    # cv2.circle(image, p2[1], 1, 25, thickness=5, lineType=8, shift=0)

    # cv2.circle(image, p1[2], 1, 1555, thickness=5, lineType=8, shift=0)
    # cv2.circle(image, p2[2], 1, 25, thickness=5, lineType=8, shift=0)

    # cv2.circle(image, p1[3], 1, 1555, thickness=5, lineType=8, shift=0)
    # cv2.circle(image, p2[3], 1, 25, thickness=5, lineType=8, shift=0)

    # cv2.imshow("Original", image )
    # cv2.waitKey(0)

    # In[ ]:

    h11 = []
    for i in range(4):
        h11.append(p1[i][0])
    for i in range(4):
        h11.append(0)
    # print h11

    h12 = []
    for i in range(4):
        h12.append(p1[i][1])
    for i in range(4):
        h12.append(0)
    # print h12

    h13 = []
    for i in range(4):
        h13.append(1)
    for i in range(4):
        h13.append(0)
    # print h13

    h21 = []
    for i in range(4):
        h21.append(0)
    for i in range(4):
        h21.append(p1[i][0])
    # print h21

    h22 = []
    for i in range(4):
        h22.append(0)
    for i in range(4):
        h22.append(p1[i][1])
    # print h22

    h23 = []
    for i in range(4):
        h23.append(0)
    for i in range(4):
        h23.append(1)
    # print h23

    h31 = []
    for i in range(4):
        h31.append(-1*p1[i][0]*p2[i][0])
    for i in range(4):
        h31.append(-1*p1[i][0]*p2[i][1])
    # print h31

    h32 = []
    for i in range(4):
        h32.append(-1*p1[i][1]*p2[i][0])
    for i in range(4):
        h32.append(-1*p1[i][1]*p2[i][1])
    # print h32

    b = []
    for i in range(4):
        b.append(p2[i][0])
    for i in range(4):
        b.append(p2[i][1])
    b = np.array(b)

    A = np.zeros((8,9))
    A[:,0] = h11
    A[:,1] = h12
    A[:,2] = h13
    A[:,3] = h21
    A[:,4] = h22
    A[:,5] = h23
    A[:,6] = h31
    A[:,7] = h32
    A[:,8] = -b
    # print A

    A = Matrix(A)
    H = A.nullspace()[0]
    H = np.array(H)
    H = H.reshape((3,3))
    # print H


    # In[ ]:
    print "Generating Transformed Image..."
    newimage = np.zeros(image.shape)
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            res = np.dot(H,np.array([x,y,1]))
            x1 = int(round(res[0]/res[2]))
            y1 = int(round(res[1]/res[2]))
            if x1>=0 and x1<image.shape[1]:
                if y1>=0 and y1<image.shape[0]:
                    newimage[y1,x1,:] = image[y,x,:]

    # cv2.imwrite("../images/res.png", newimage)
    # newimage = cv2.imread('../images/res.png')
    # cv2.imshow("Transformed", newimage)

    # In[ ]:

    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(newimage, cv2.MORPH_CLOSE, kernel)

    # cv2.imwrite("../images/resC.png", closing)
    # closing = cv2.imread('../images/resC.png')
    # cv2.imshow("Transformed and Closed", closing)

    # cv2.waitKey(0)

    return [newimage, closing]
