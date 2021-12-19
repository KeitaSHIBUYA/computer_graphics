import cv2
import os
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"salt_pepper.png", cv2.IMREAD_GRAYSCALE)
# print(img)

kernel = np.ones((5,5),np.uint8)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
result = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)


cv2.imshow("result", result)

k = cv2.waitKey(0)
if k == ord('q'):				# When the Q key is pressed, it's done.
    cv2.destroyAllWindows()