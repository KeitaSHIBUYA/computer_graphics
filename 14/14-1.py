import cv2
import os
import numpy as np

imgL = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/TSUKUBA_LEFT.png",0)
imgR = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/TSUKUBA_RIGHT.png",0)

###  Stereo matching using the Block Matching method (numDisparities=32, blockSize=15)  ###
stereo = cv2.StereoBM_create(numDisparities=32, blockSize=15)
disp = stereo.compute(imgL, imgR)
width, height = disp.shape


###  Define the uint8 array result filled by zeros as same size as disp  ###
result = np.zeros((width, height), np.uint8)
# print(result)
###  Normalize disp image to range [min of disp, max of disp] & convert image type to uint8 using cv2.normalize function  ###
result = cv2.normalize(disp, result, np.min(disp), np.max(disp), norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
result = result.astype(np.uint8)

cv2.imshow("disp", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
