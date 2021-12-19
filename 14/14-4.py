import cv2
import numpy as np
import os

### 画像の読み込み
img1 = cv2.imread(os.path.dirname(
	os.path.abspath(__file__))+"/ball_light1.bmp", 0)
img2 = cv2.imread(os.path.dirname(
	os.path.abspath(__file__))+"/ball_light2.bmp", 0)
img3 = cv2.imread(os.path.dirname(
	os.path.abspath(__file__))+"/ball_light3.bmp", 0)
img4 = cv2.imread(os.path.dirname(
	os.path.abspath(__file__))+"/ball_light4.bmp", 0)
color = cv2.imread(os.path.dirname(
	os.path.abspath(__file__))+"/ball_light1.bmp")

### 光源の行列
s = np.array([[ 10,  10, 10],
              [-10,  10, 10],
              [-10, -10, 10],
              [ 10, -10, 10]])

### 転置
S = s.T

### 画像の大きさを取得
height, width = img1.shape
h, w, c = color.shape


list = np.array([[0],
                 [0],
                 [0],
                 [0]])

RGB = np.array([0, 0, 0])


color_map = np.zeros((h, w, c), np.uint8)
dst = np.zeros((h, w, c), np.uint8)



for i in range(height):
    for j in range(width):
        list[0] = img1[i, j]
        list[1] = img2[i, j]
        list[2] = img3[i, j]
        list[3] = img4[i, j]

        result = np.linalg.inv(S @ s) @ S @ list

        # result2 = cv2.normalize(result, dst, -1, 1, norm_type=cv2.NORM_L2)
        result2 = result / np.linalg.norm(result)

        RGB[0] = ((255 / 2) * (result2[0] + 1)).astype(np.uint8)
        RGB[1] = ((255 / 2) * (result2[1] + 1)).astype(np.uint8)
        RGB[2] = ((255 / 2) * (result2[2] + 1)).astype(np.uint8)

        color_map[i, j] = RGB




BGR = cv2.cvtColor(color_map, cv2.COLOR_RGB2BGR)



cv2.imshow("Calclated normal map", BGR)
k = cv2.waitKey(0)
if k == ord('q'): 				# When the Q key is pressed, it's terminated.
    cv2.destroyAllWindows()