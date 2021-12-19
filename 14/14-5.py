import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

img1 = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/bunnies_left1.bmp",0)
img2 = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/bunnies_right1.bmp",0)

# print(img1)

sift = cv2.SIFT_create()