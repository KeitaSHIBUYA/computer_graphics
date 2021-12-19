import cv2
import os
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/coin_illust.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray, 150, 100, L2gradient=True)
# cv2.imshow("edge", edges)

# lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)
lines = cv2.HoughLinesP(edges, 1, np.pi / 250, threshold=100, maxLineGap=100)

if lines is not None:
    for x1, y1, x2, y2 in lines.squeeze(axis=1):
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Result", img)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()