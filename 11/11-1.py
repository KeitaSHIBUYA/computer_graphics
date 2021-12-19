import cv2
import os
import numpy as np


def calculate_ManhattanDistanceMap(img):
    height, width = img.shape
    ### Define the uint8 array dist_map filled by zeros as same size as img. ###
    dist_map = np.zeros((height, width), np.uint8)
    # dist_map = np.uint8(np.zeros(height, width))
    # print(dist_map)
    for i in range(height):
        for j in range(width):
            if img[i][j] > 0:
                # Set a large distance value once where the pixels exist.
                dist_map[i][j] = 255

    for i in range(1, height):
        for j in range(1, width):
            ### Let VAL be the minimum value among (the value next to left) + 1, (the value of below) + 1 and oneself. ###
            val = np.amin(
                np.array([dist_map[i][j-1] + 1, dist_map[i-1][j] + 1, dist_map[i][j]]))
            dist_map[i][j] = val

    for i in range(height-2, 0, -1):
        for j in range(width-2, 0, -1):
            ### Let VAL be the minimum value among (the value next to right) + 1, (the value of above) + 1 and oneself. ###
            val = np.amin(
                np.array([dist_map[i][j+1] + 1, dist_map[i+1][j] + 1, dist_map[i][j]]))
            dist_map[i][j] = val

    return dist_map


src = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/input_image.png", cv2.IMREAD_GRAYSCALE)		# Load an image

dist_map = calculate_ManhattanDistanceMap(src)
# Normalize dist_map to confirm it easily.
dist_map_norm = np.uint8(dist_map/np.amax(dist_map)*255)

cv2.imshow("src", src)
cv2.imshow("distance map", dist_map)
cv2.imshow("normalized distance map", dist_map_norm)

k = cv2.waitKey(0)
if k == ord('q'):				# When the Q key is pressed, it's done.
    # cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/11-1_distance_map.bmp", dist_map)
    # cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/11-1_distance_map_norm.bmp", dist_map_norm)
    cv2.destroyAllWindows()
