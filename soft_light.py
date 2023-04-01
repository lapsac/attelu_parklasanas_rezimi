#režīms: Soft light
#====================================
# matematiska funkcija filtram soft light:
#if A<=0.5 then
#C=(2*A-1)*(B-B^2)+B
#if A >0.5 then
#C=(2*A-1)*(sqrt(B)-B)+B
#
#A-priekšplāna attēls
#B-fona attels
#C-rezultats
#====================================
import numpy as np
from numpy import asarray
import math
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
image_A = cv2.imread('koks.png')
image_B = cv2.imread('kalni.png')
im_rgb_A = cv2.cvtColor(image_A, cv2.COLOR_BGR2RGB)
im_rgb_B = cv2.cvtColor(image_B, cv2.COLOR_BGR2RGB)

cv2.imwrite('koks.png', resized_img_A)
cv2.imwrite('kalni.png', resized_img_B)
soft_light = np.where((image_norm_A <= 0.5),
                      (2 * image_norm_A - 1) * image_norm_B - (image_norm_B)**2 + image_norm_B,
                      (2 * image_norm_A - 1) * (np.sqrt(image_norm_B) - image_norm_B) + image_norm_B)

fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(1,3,1)
ax1.title.set_text('input img 1')
ax1.imshow(image_norm_A)
ax2 = fig.add_subplot(1,3,2)
ax2.title.set_text('input img 2')
ax2.imshow(image_norm_B)
ax3 = fig.add_subplot(1,3,3)
ax3.title.set_text('Soft Light')
ax3.imshow(soft_light)
