import numpy as np
import argparse
import cv2
import math
from sympy import Matrix

def dlt(p1, p2 ):

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

    return H
