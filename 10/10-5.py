import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import laplace
from skimage import io

src_img = io.imread(os.path.dirname(os.path.abspath(__file__)) +
               "/src.png",) / 255.0
target_img = io.imread(os.path.dirname(os.path.abspath(__file__)) +
               "/target.png",) / 255.0
mask_img = io.imread(os.path.dirname(os.path.abspath(__file__)) +
               "/mask.png") == 255


src_coords = np.argwhere(mask_img)
src_top, src_left = np.min(src_coords, axis=0) - 1
src_bottom, src_right = np.max(src_coords, axis=0) + 1
mask_patch = mask_img[src_top : src_bottom + 1, src_left : src_right + 1]
src_patch = src_img[src_top : src_bottom + 1, src_left : src_right + 1]


target_top, target_left = (src_top + target_img.shape[0] - src_img.shape[0], 30)
target_bottom, target_right = (
    target_top + mask_patch.shape[0],
    target_left + mask_patch.shape[1],
)
target_patch = target_img[target_top:target_bottom, target_left:target_right]

def poisson_blend(target_img, src_img, mask_img, iter: int = 1024):
    for _ in range(iter):
        target_img = target_img + 0.25 * mask_img * laplace(target_img - src_img)
    return target_img.clip(0, 1)


blend_patch = np.stack(
    [
        poisson_blend(target_patch[:, :, i], src_patch[:, :, i], mask_patch)
        for i in range(3)
    ],
    axis=2,
)


# plt.figure(figsize=(64, 64))
# plt.subplot(1, 4, 1)
# io.imshow(src_patch)
# plt.subplot(1, 4, 2)
# plt.imshow(mask_patch)
# plt.subplot(1, 4, 3)
# io.imshow(target_patch)
# plt.subplot(1, 4, 4)
io.imshow(blend_patch)
plt.show()
