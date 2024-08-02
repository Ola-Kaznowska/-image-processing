import cv2 
import numpy as np  
import math  


def flip_image(img):
    new_img = []
    for row in range(img.shape[0]):
        new_row = []
        for column in range(img.shape[1]):
            new_row.append(img[row][-column-1])
        new_img.append(new_row)
    return np.array(new_img)


filename = "test.jpeg"

img = cv2.imread(filename)
cv2.imshow("Obraz bez modyfikacji", img)
cv2.waitKey(0)


img = cv2.imread(filename)
img = flip_image(img)
cv2.imshow("Lustrzanie odbicie", img)
cv2.waitKey(0)