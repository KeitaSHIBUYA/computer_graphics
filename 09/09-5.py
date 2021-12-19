from skimage.metrics import structural_similarity as ssim
import os
import cv2

img1 = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"Cameraman.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"Cameraman.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"Cameraman.jpg", cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"Cameraman_noise.bmp", cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                 "/"+"LENNA.bmp", cv2.IMREAD_GRAYSCALE)


print("Cameraman.bmp vs Cameraman.png =>", ssim(img1, img2))
print("Cameraman.bmp vs Cameraman.jpg =>", ssim(img2, img3))
print("Cameraman.bmp vs Cameraman_noise.bmp =>", ssim(img1, img4))
print("Cameraman.bmp vs LENNA.bmp =>", ssim(img1, img5))


print(img1)