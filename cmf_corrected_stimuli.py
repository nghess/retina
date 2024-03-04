import numpy as np
import cv2

# Set up canvas
size = 1024
origin = (size//2, size//2)
canvas = np.zeros((size,size), dtype=np.uint8)
cv2.circle(canvas, origin, radius=size//2-3, color=64, thickness=3)

# Draw stimulus function
def stim_mask(location:tuple, f_size:int):
    assert len(location) == 2, "Location must be a 2-tuple containing (polar angle, eccentricity)."
    # assert location[0] <= 360, "Polar angle cannot exceed 360 degrees."
    # assert location[1] <= 90, "Eccentricity cannot exceed 90 degrees."
    
    

    x = location[0] + origin[0]
    y = origin[1] - location[1]

    # Calculate stimulus size
    distance = np.sqrt(location[0]**2 + location[1]**2)
    eccentricity = (distance / origin[0]) * 90
    
    radius = int(f_size * np.exp(eccentricity*.1))

    print(eccentricity)
    print(radius)

    cv2.circle(canvas, (x,y), radius=radius, color=255, thickness=1)

stim_mask((0,50), 5)
stim_mask((0,30), 5)
stim_mask((0,0), 5)

cv2.imshow("retina", canvas)
cv2.waitKey(0)