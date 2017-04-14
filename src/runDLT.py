import numpy as np
import argparse
import cv2
import math
from sympy import Matrix
from dlt import *

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help = "path to the image file")
# ap.add_argument("-p1", "--p1", help = "Four Points in Original Image")
# ap.add_argument("-p2", "--p2", help = "Four Points in Transformed Image")
# args = vars(ap.parse_args())

# image = cv2.imread(args['image'])
# p1  = args['p1']
# p2  = args['p2']

# image = cv2.imread('../images/note.png')

####---------------- note.png
# p1  = [(73,239), (356,117), (475,265), (187,443)]
# p2  = [(73,239), (365,239), (365,450), (73,450)]

# image = cv2.imread('../images/house.jpg')

####----------------- house.jpg --- res1
# p1  = [(82,215), (82,80), (287,120), (287,202)]
# p2  = [(50,215), (50,80), (290,80), (290,215)]

# image = cv2.imread('../images/roadsign.jpg')

#### ----------------- roadsign.jpg --- res1
# p1  = [(119,207), (119,267), (380,164), (380,227)]
# p2  = [(119,207), (119,267),(400,207), (400,267)]

####----------------- roadsign.jpg --- res2
# p1  = [(105,60), (105,120), (377,126), (377,186)]
# p2  = [(105,60), (105,120), (390,60), (390,120)]

image = cv2.imread('../images/house2.jpg')

#----------------- house2.jpg --- res1
# p1  = [(490,340), (605,338), (490,487), (603,468)]
# p2  = [(490,340),(645,340), (490,487), (645,487)]

##----------------- house2.jpg --- res2
p1  = [(310,205), (310,477), (119,274), (119,410)]
p2  = [(310,205), (310,477), (45,205), (45,477)]

# cv2.circle(image, p1[0], 1, 1555, thickness=5, lineType=8, shift=0)
# cv2.circle(image, p2[0], 1, 25, thickness=5, lineType=8, shift=0)

# cv2.circle(image, p1[1], 1, 1555, thickness=5, lineType=8, shift=0)
# cv2.circle(image, p2[1], 1, 25, thickness=5, lineType=8, shift=0)

# cv2.circle(image, p1[2], 1, 1555, thickness=5, lineType=8, shift=0)
# cv2.circle(image, p2[2], 1, 25, thickness=5, lineType=8, shift=0)

# cv2.circle(image, p1[3], 1, 1555, thickness=5, lineType=8, shift=0)
# cv2.circle(image, p2[3], 1, 25, thickness=5, lineType=8, shift=0)


cv2.imshow("Original", image )
# cv2.waitKey(0)
[newimage, closing] = dlt(image, p1, p2)

cv2.imwrite("../images/res.png", newimage)
newimage = cv2.imread('../images/res.png')
cv2.imshow("Transformed", newimage)

cv2.imwrite("../images/resC.png", closing)
closing = cv2.imread('../images/resC.png')
cv2.imshow("Transformed and Closed", closing)

cv2.waitKey(0)
