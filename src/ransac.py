import numpy as np
from directlt import dlt

def ransac(pts1, pts2, N=10, t=0.90, thresh=4.0, ):

    # thresh = 4.0
    # N = 10
    # t = 0.95
    totalPoints = len(pts1)

    bestH = np.zeros((3,3))
    maxInliers = 0

    for j in range(N):

        randFour = [np.random.randint(0,totalPoints) for i in range(4)]
        p1 = pts1[randFour]
        p2 = pts2[randFour]
        H = dlt(p1,p2)

        inLiers = 0
        for ind in range(totalPoints):
            source = pts1[ind]
            target = np.array([pts2[ind][0],pts2[ind][1]])
        #     print target

            pred = np.dot(H, np.array([source[0],source[1],1]))
            predx = pred[0]/pred[2]
            predy = pred[1]/pred[2]
            pred = np.array([predx,predy])
            pred = np.float32([point for point in pred])
        #     print pred
            np.linalg.norm(target-pred)
            if np.linalg.norm(target-pred) < thresh:
                inLiers += 1
    #     print inLiers, t*totalPoints

        if maxInliers < inLiers:
            maxInliers = inLiers
            bestH = H
            if inLiers > t*totalPoints:
                break
    return bestH

