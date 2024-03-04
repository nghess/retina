import cv2
import numpy as np

"""
Average Blur: A sanity check
"""

c_sz = 512  # Canvas size
k_sz = 15  # Kernel size
kernel = np.ones([k_sz, k_sz]) * (1/k_sz**2)  # Averaging kernel

# Initialize canvas and draw something
canvas = np.zeros([c_sz, c_sz], dtype=np.uint8)
cv2.circle(canvas, (c_sz//2, c_sz//2), 51, (255), -1)

# Pad Canvas for kernel
padded_canvas = np.pad(canvas, ((k_sz//2, k_sz//2), (k_sz//2, k_sz//2)), mode='constant', constant_values=0)

# Create output matrix with original canvas size
output = np.zeros_like(canvas)

# 2d convolution across image
for x in range(c_sz):
    for y in range(c_sz):
        output[x, y] = np.sum(padded_canvas[x:x+k_sz, y:y+k_sz] * kernel)

# Display blurred image
cv2.imshow("avg blur", output)
cv2.waitKey(0)

