import cv2 as cv
import numpy as np

# HSV values for colors (yellow = 0, blue = 1, red = 2, green = 3, white = 4, orange = 5)
lower_yellow = np.array([25, 100, 100])
upper_yellow = np.array([40, 255, 255])

lower_blue = np.array([100, 100, 100])
upper_blue = np.array([130, 255, 255])

# Red has 2 gap values
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([20, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 30, 255])

lower_orange = np.array([10, 100, 100])
upper_orange = np.array([25, 255, 255])


img = cv.imread('onbir.jpg')

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(img_hsv, lower_yellow, upper_yellow)

# Detect the yellow areas
yellow_pixels = np.where(mask > 0)

result_matrix = np.zeros((3, 3), dtype=int)

# Divide the image by 9 and find the pixels with the corresponding color

for y, x in zip(yellow_pixels[0], yellow_pixels[1]):
    result_matrix[y // (img.shape[0] // 3)][x // (img.shape[1] // 3)] = 1

cv.imshow('test',mask)
cv.waitKey()
print(result_matrix)
