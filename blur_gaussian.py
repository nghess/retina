import cv2
import numpy as np

"""
Gaussian Blur: A sanity check
"""

def generate_gaussian_kernel(k_size, sigma):

    # Ensure kernel has a central pixel
    assert k_size % 2 == 1, "Kernel size must be odd."
    
    # Initialize the kernel
    kernel = np.zeros((k_size, k_size))
    
    # Define center of Gaussian
    mu = k_size // 2
    
    # Compute the kernel values
    for x in range(k_size):
        for y in range(k_size):
            dx = x - mu
            dy = y - mu
            kernel[x, y] = (1 / (2 * np.pi * sigma**2)) * np.exp(-(dx**2 + dy**2) / (2 * sigma**2))
    
    # Normalize the kernel to ensure the sum of all elements equals 1
    kernel /= np.sum(kernel)
    
    return kernel

c_sz = 512  # Canvas size
k_sz = 5  # Kernel size
kernel = generate_gaussian_kernel(k_sz, k_sz/3)

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
cv2.imshow("gaussian blur", output)
cv2.waitKey(0)