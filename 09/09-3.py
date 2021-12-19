import os
import cv2
import numpy as np
from numpy.ma import count
from scipy import stats

src = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"Cameraman.bmp", cv2.IMREAD_GRAYSCALE)		# Load an image
# print(os.path.dirname(os.path.abspath(__file__))+"/"+"Cameraman.bmp")				# for debug
# print(src)
src_float = src.astype(np.float32)

max = np.max(src_float)
min = np.min(src_float)
mean = np.mean(src_float)
var = np.var(src_float)
median = np.median(src_float)
mode, count = stats.mode(src_float, axis=None)

print("max:", max)
print("min:",min)
print("mean:",mean)
print("var:",var)
print("median:",median)
print("mode:",float(mode))