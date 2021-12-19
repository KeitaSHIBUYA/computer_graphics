import os
import cv2
import numpy as np
import sys


# 画像をグレースケールで読み込み
src = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                      "/"+"input_image.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 二値変換
mono_src = cv2.threshold(gray, 48, 255, cv2.THRESH_BINARY)[1]

# ラベリング処理
label = cv2.connectedComponentsWithStats(gray)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mono_src)
# print(stats)

stats = label[2]
area = stats[:, cv2.CC_STAT_WIDTH] * stats[:, cv2.CC_STAT_HEIGHT]
idx = area.argsort()[-4:-1]  # 2番目、3番めに面積が大きいラベル (1番目は背景なので除く)
# print(idx)

# オブジェクト情報を項目別に抽出
data = label[2]
center = label[3]

# ラベリング結果書き出し用に二値画像をカラー変換
color_src01 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# ラベルに応じて、色をつけた画像を作成
color_src01[labels == 0] = [0, 0, 0]      # 背景ラベル
color_src01[labels == 1] = [255, 0, 0]    # ラベル1
color_src01[labels == 2] = [0, 255, 0]    # ラベル2
color_src01[labels == 3] = [0, 0, 255]  # ラベル3

# cv2.imshow('dst', dst)

height, width = mono_src.shape[:2]
blue = [255, 0, 0]
green = [0, 255, 0]
red = [0, 0, 255]


# オブジェクト情報を利用してラベリング結果を画面に表示
for i in idx:
    # 各オブジェクトの外接矩形を赤枠で表示
    x0 = data[i][0]
    y0 = data[i][1]
    x1 = data[i][0] + data[i][2]
    y1 = data[i][1] + data[i][3]
    cv2.rectangle(color_src01, (x0, y0), (x1, y1), (0, 0, 255))

    # 各オブジェクトのラベル番号と面積に黄文字で表示
    cv2.putText(color_src01, "ID: " + str(i + 1), (x1 - 50, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
    cv2.putText(color_src01, "S: " + str(data[i][4]), (x1 - 50, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

    # 各オブジェクトの重心座標をに黄文字で表示
    cv2.putText(color_src01, "X: " + str(int(center[i][0])), (x1 - 110, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
    cv2.putText(color_src01, "Y: " + str(int(center[i][1])), (x1 - 110, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

# 結果の表示
cv2.imshow("output", color_src01)

k = cv2.waitKey(0)
if k == ord('q'):				# When the Q key is pressed, it's done.
    cv2.destroyAllWindows()