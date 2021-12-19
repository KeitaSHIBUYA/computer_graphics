import cv2
import os
import numpy as np

src = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/Lenna_color.bmp", cv2.IMREAD_COLOR)		# Load an image


for i in range(10):
    src = cv2.bilateralFilter(src, 15, 20, 20)
    if i == 0:
        cv2.imshow("once", src)
    elif i == 1:
        cv2.imshow("twice", src)
    elif i == 9:
        cv2.imshow("ten_times", src)


k = cv2.waitKey(0)
if k == ord('q'): 				# When the Q key is pressed, it's done.
    # cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/10-1_sobel.bmp", result)
    cv2.destroyAllWindows()
