import cv2
import os
import numpy as np

src = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/WOMAN.bmp",0)
src2 = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/HORSE.bmp",0)

ft = np.fft.fft2(src) # 2D FFT
ft2 = np.fft.fft2(src2) 

ft = np.fft.fftshift(ft) # Shift the data so that the DC component is in the center
ft2 = np.fft.fftshift(ft2) 

Pow = np.abs(ft)**2 # Calculate power spectrum
Pow2 = np.abs(ft2)**2 

Pow = np.log10(Pow) # Please ignore the warnings of this line
Pow2 = np.log10(Pow2) 

Pmax = np.max(Pow)
Pmax2 = np.max(Pow2)

Pow = Pow / Pmax * 255
Pow2 = Pow2 / Pmax2 * 255

pow_img = Pow.astype(np.uint8)
pow_img2 = Pow2.astype(np.uint8)

h, w = ft.shape
mask = np.zeros((h, w))
centery = w/2
R = 20
for x in range(0, h):
    for y in range(0, w):
        ### If statement where the inside of the radius R is 1 ###
        if (x - centery) ** 2 + (y - centery) ** 2 < R ** 2:
            mask[x, y] = 1

### Calculate lowpass result on frequency space using mask and Fourier transform result ###
lowpass = ft * mask
lowpass = np.fft.ifftshift(lowpass)

### Calculate inverse Fourier transform of lowpass ###
dst = np.fft.ifft2(lowpass)
dst = np.abs(dst)
dst_img = np.uint8(dst)

h, w = ft2.shape
mask = np.zeros((h, w))
centery = w / 2
R = 20
for x in range(0, h):
    for y in range(0, w):
        if (x - centery) ** 2 + (y - centery) ** 2 > R ** 2:
            mask[x, y] = 1

highpass = ft2 * mask
highpass = np.fft.ifftshift(highpass)

dst2 = np.fft.ifft2(highpass)
dst2 = np.abs(dst2)

dst_img2 = np.uint8(dst2)


result = cv2.add(dst_img, dst_img2)


cv2.imshow("result", result)
k = cv2.waitKey(0)
if k == ord('q'): 				# When the Q key is pressed, it's done.
    cv2.destroyAllWindows()