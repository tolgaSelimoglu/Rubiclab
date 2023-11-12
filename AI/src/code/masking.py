import cv2 as cv
import numpy as np
import glob


def moves_to_urfdlb(src_path, target_path):

    results = get_pic_paths(src_path)
"""
ezgi kod buraya
target_path src/data/cube_colours.txt
olacak
içine urfdlb diye kaydedecek
"""


def get_pic_paths(src_path):

    results = []
    print("Getting image paths")
    image_paths = glob.glob(src_path + 'cube_face*.jpg')
    print(image_paths)
    for path in image_paths:
        results.append(convert(path))

    print(results)
    return results

def convert(path):

    print("Converting images")
    lower_bounds = [
        np.array([20, 100, 100]),  # Yellow
        np.array([100, 100, 100]),  # Blue
        np.array([0, 95, 100]),  # Red (1. gap)
        np.array([160, 95, 100]),  # Red (2. gap)
        np.array([40, 100, 100]),  # Green
        np.array([0, 0, 195]),       # White
        np.array([2, 100, 100])  # Orange
    ]

    upper_bounds = [
        np.array([40, 255, 255]),  # Yellow
        np.array([130, 255, 255]),  # Blue
        np.array([20, 255, 255]),  # Red (1. gap)
        np.array([180, 255, 255]),  # Red (2. gap)
        np.array([80, 255, 255]),  # Green
        np.array([180, 100, 255]),    # White
        np.array([25, 255, 255])  # Orange
    ]

    picsel_centers = [(50,50), (50,150), (50,250),
                  (150,50), (150,150), (150, 250),
                  (250,50), (250,150), (250,250)]

    color_names = ['Yellow', 'Blue', 'Red', 'Red', 'Green', 'White', 'Orange']

    img = cv.imread('pics/ezgi.jpg')
    resized_img = cv.resize(img, (300, 300))
    img_hsv = cv.cvtColor(resized_img, cv.COLOR_BGR2HSV)

    result_matrix = np.empty((3, 3), dtype='<U10')
    neighborhood_size = 3

    for i in range(7):
        mask = cv.inRange(img_hsv, lower_bounds[i], upper_bounds[i])

        for center_x, center_y in picsel_centers:
            # Define the neighborhood around the current center
            neighborhood = img_hsv[center_y - neighborhood_size:center_y + neighborhood_size + 1,
                                   center_x - neighborhood_size:center_x + neighborhood_size + 1, :]

            # Calculate the average HSV values for the neighborhood
            avg_hsv = np.median(neighborhood, axis=(0, 1))

            # Check if the average HSV values are within the specified range
            if np.all(np.logical_and(lower_bounds[i] <= avg_hsv, avg_hsv <= upper_bounds[i])):
                # Update the result matrix or perform any other desired operation
                result_matrix[center_y // 100, center_x // 100] = color_names[i]

    cv.waitKey()

    return result_matrix
