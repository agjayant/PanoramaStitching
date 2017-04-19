
# coding: utf-8

# In[ ]:

import numpy as np
import argparse
import imutils
import cv2
import math
from sympy import Matrix


def matchPoints(image1, image2):


    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)


    sift = cv2.xfeatures2d.SIFT_create()
    (points1, features1) = sift.detectAndCompute(image1, None)

    sift = cv2.xfeatures2d.SIFT_create()
    (points2, features2) = sift.detectAndCompute(image2, None)


    points1 = np.float32([point.pt for point in points1])
    points2 = np.float32([point.pt for point in points2])



    matchPoints = cv2.DescriptorMatcher_create("BruteForce")
    rawMatches = matchPoints.knnMatch(features1, features2, 2)


    matches = []
    for m in rawMatches:
        if len(m) == 2 and m[0].distance < m[1].distance * 0.75:
            matches.append((m[0].trainIdx, m[0].queryIdx))



    # computing a homography requires at least 4 matches
    if len(matches) <= 4:
        assert(1==2),"Less than 4 matches"

    pts1 = np.float32([points1[i] for (_, i) in matches])
    pts2 = np.float32([points2[i] for (i, _) in matches])

    return [ pts1 , pts2 ]
