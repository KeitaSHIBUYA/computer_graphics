'''
自分の環境ではカメラを複数接続していたのでcv2.VideoCapture(1)になっています。
'''


import cv2
import numpy as np

square_size = 2.2       # One side length of a chessboard square [cm]
pattern_size = (7, 7)   # Number of intersection points
reference_img = 20      # The number of reference images

# Specify the chessboard coordinates (X,Y,0)
pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 )
pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
pattern_points *= square_size
objpoints = []
imgpoints = []

# Capture images from camera
capture = cv2.VideoCapture(1)

while len(objpoints) < reference_img:
    ret, img = capture.read()
    height = img.shape[0]
    width = img.shape[1]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting chessboard corners
    ret, corner = cv2.findChessboardCorners(gray, pattern_size)
    # If found, add object points, image points and draw chessboard corners
    if ret == True:
        print("Detect Chess Board Coners")
        print(str(len(objpoints)+1) + "/" + str(reference_img))
        term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
        corners = cv2.cornerSubPix(gray, corner, (5,5), (-1,-1), term)
        imgpoints.append(corner.reshape(-1, 2))
        objpoints.append(pattern_points)
        ###  Draw chessboard corners using drawChessboardCorners  ###
        img = cv2.drawChessboardCorners(img, pattern_size, corners,ret)

    cv2.imshow('image', img)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

print("Calculating camera parameter...")
###  Calculate internal camera parameters & store error and the camera matrix to err and mtx, respectively  ###
err, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

###  Calculate aspect ratio by f_y/f_x  ###
aspect_ratio = pattern_size[0] / pattern_size[1]

print("RMS = ", err)
print(mtx)
print("Aspect Ratio = ", aspect_ratio)