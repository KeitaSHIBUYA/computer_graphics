import math
import numpy as np


def calcTriangleArea(p1, p2, p3):
    v1 = np.array(p1)
    v2 = np.array(p2)
    v3 = np.array(p3)
    # Calculate a cross vector using v1, v2, v3 ##
    cross_vector = np.cross((v1 - v2),(v2 - v3))
    # Calculate the triangle area using cross_vector ##
    area = np.sqrt((cross_vector[0] ** 2) + (cross_vector[1] ** 2) + (cross_vector[2] **2)) / 2
    return area


def main():
    print(calcTriangleArea([2, 0, 0], [0, 2, 0], [0, 0, 2]))
    print(calcTriangleArea([0, 0, 0], [
          1, math.sqrt(3), 0], [-1, math.sqrt(3), 0]))


if __name__ == "__main__":
    main()
