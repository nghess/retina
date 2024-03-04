import numpy as np
import cv2
import matplotlib.pyplot as plt

steps = 256
theta = np.linspace(0, 2*np.pi, steps)
radius = 100
c_sz = 512
origin = c_sz//2

wave = np.sin(np.linspace(0, 32*np.pi, steps)) * 10
wavx = np.linspace(0, steps, steps)

x = np.cos(theta) * (wave + radius)
y = np.sin(theta) * (wave + radius)

canvas = np.zeros([c_sz,c_sz], dtype=np.uint8)

for ii in range(steps):
    canvas[int(x[ii])+origin,int(y[ii])+origin] = 255

cv2.imshow('circle', canvas)
cv2.waitKey(0)

