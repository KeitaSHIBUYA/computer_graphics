import cv2
import os
import numpy as np

src = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/LENNA.bmp",0)
ft = np.fft.fft2(src) # 2D FFT
ft = np.fft.fftshift(ft) # Shift the data so that the DC component is in the center

Pow = np.abs(ft)**2 # Calculate power spectrum
Pow = np.log10(Pow) # Please ignore the warnings of this line
Pmax = np.max(Pow)
Pow = Pow / Pmax * 255
pow_img = Pow.astype(np.uint8)
# cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/LENNA_FFT.bmp", pow_img)

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

cv2.imshow("result", dst_img)
k = cv2.waitKey(0)
if k == ord('q'): 				# When the Q key is pressed, it's done.
    # cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/10-2.bmp", dst_img)
    cv2.destroyAllWindows()