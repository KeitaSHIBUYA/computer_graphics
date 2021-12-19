import os
import random
import sys

import cv2
import numpy as np
from numpy.lib import index_exp


# 画像をグレースケールで読み込み
gray_src = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"input_image.png", 0)

# 二値変換
mono_src = cv2.threshold(gray_src, 48, 255, cv2.THRESH_BINARY)[1]

# ラベリング処理
id, markers = cv2.connectedComponents(mono_src)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mono_src)
# print(labels)

# ラベリング結果書き出し準備
color_src = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)
height, width = mono_src.shape[:2]
# print(height, width)


blue = [255, 0, 0]
green = [0, 255, 0]
red = [0, 0, 255]

# ラベリング結果を画面に表示
for y in range(0, height):
    for x in range(0, width):
        if labels[y, x] == 1:
            color_src[y, x] = blue
        elif labels[y, x] == 2:
            color_src[y, x] = green
        elif labels[y, x] == 3:
            color_src[y, x] = red
        else:
            color_src[y, x] = [0, 0, 0]



# 結果の表示
cv2.imshow("color_src", color_src)

k = cv2.waitKey(0)
if k == ord('q'):				# When the Q key is pressed, it's done.
    cv2.destroyAllWindows()