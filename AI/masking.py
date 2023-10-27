import cv2 as cv
import numpy as np

# HSV values for colors (yellow = 0, blue = 1, red = 2, green = 3, white = 4, orange = 5)
lower_bounds = [
    np.array([25, 100, 100]),  # Yellow
    np.array([100, 100, 100]),  # Blue
    np.array([0, 100, 100]),  # Red (1. gap)
    np.array([160, 100, 100]),  # Red (2. gap)
    np.array([35, 100, 100]),  # Green
    #   np.array([0, 0, 200]),       # White
    np.array([10, 100, 100])  # Orange
]

upper_bounds = [
    np.array([40, 255, 255]),  # Yellow
    np.array([130, 255, 255]),  # Blue
    np.array([20, 255, 255]),  # Red (1. gap)
    np.array([179, 255, 255]),  # Red (2. gap)
    np.array([85, 255, 255]),  # Green
    # np.array([180, 30, 255]),    # White
    np.array([25, 255, 255])  # Orange
]

img = cv.imread('pics/baho3.jpg')
resized_img = cv.resize(img, (305, 310))
img_hsv = cv.cvtColor(resized_img, cv.COLOR_BGR2HSV)

result_matrix = np.zeros((3, 3), dtype=int)
for i in range(6):
    mask = cv.inRange(img_hsv, lower_bounds[i], upper_bounds[i])

    # Detect the yellow areas
    color_pixels = np.where(mask > 0)

    # Divide the image by 9 and find the pixels with the corresponding color
    for y, x in zip(color_pixels[0], color_pixels[1]):
        if i > 2:
            result_matrix[y // (img.shape[0] // 3)][x // (img.shape[1] // 3)] = i - 1
        else:
            result_matrix[y // (img.shape[0] // 3)][x // (img.shape[1] // 3)] = i

cv.imshow('test', mask)
cv.waitKey()
print(result_matrix)
