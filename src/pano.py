import numpy as np
import argparse
import imutils
import cv2
import math
from sympy import Matrix
from directlt import dlt
from ransac import ransac
from matchPoints import matchPoints

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--left", help = "Path to left image file")
ap.add_argument("-r", "--right", help = "Path to right image file")
args = vars(ap.parse_args())


# image2 = cv2.imread('images/bryce_left_02.png')
# image1 = cv2.imread('images/bryce_right_02.png')

image2 = cv2.imread(args['left'])
image1 = cv2.imread(args['right'])

image2 = imutils.resize(image2, width=400)
image1 = imutils.resize(image1, width=400)

[pts1 , pts2] = matchPoints(image1, image2)

H = ransac(pts1,pts2, 20, 0.98, 4.0) ## N, t, thresh
H = np.float64([pt for pt in H])

result = cv2.warpPerspective(image1, H,(image1.shape[1] + image2.shape[1], image1.shape[0]))
result[0:image2.shape[0], 0:image2.shape[1]] = image2

cv2.imwrite('images/result.png', result)
