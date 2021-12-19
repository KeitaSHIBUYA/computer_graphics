import os
import cv2
import numpy as np
import sys
from IPython import display
from matplotlib import pyplot as plt


def imshow(img, format=".jpg", **kwargs):
    """ndarray 配列をインラインで Notebook 上に表示する。
    """
    img = cv2.imencode(format, img)[1]
    img = display.Image(img, **kwargs)
    display.display(img)


# 画像読み込み
img = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                      "/"+"INIAD_logo.png")
# グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二値変換
ret, bin_img = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('test', bin_img)

# 輪郭を抽出する。
contours, hierarchy = cv2.findContours(
    bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# 小さい輪郭は誤検出として削除する
contours = list(filter(lambda x: cv2.contourArea(x) > 100, contours))

# 輪郭を描画する。
cv2.drawContours(img, contours, -1, color=(0, 0, 255), thickness=2)

cv2.imshow('img', img)

# 結果の表示
# cv2.imshow("output", color_src01)

k = cv2.waitKey(0)
if k == ord('q'):				# When the Q key is pressed, it's done.
    cv2.destroyAllWindows()
