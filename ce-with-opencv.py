# canny edge with opencv

import cv2
import time
import os

def use_laplace(img):
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    return cv2.convertScaleAbs(laplacian)

def use_sobel(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    sobel = sobelx + sobely
    return cv2.convertScaleAbs(sobel)

def use_canny(img):
    return cv2.Canny(img, 50, 100)

if not os.path.exists('canny-edge'):
    os.makedirs('canny-edge')

img = cv2.imread('images/a.jpg', 0)

start_time_canny = time.time()

canny = use_canny(img)

time_taken_canny = time.time() - start_time_canny
print("%.4f seconds for Canny" % time_taken_canny)

start_time_laplacian = time.time()

laplacian = use_laplace(img)

time_taken_laplacian = time.time() - start_time_laplacian
print("%.4f seconds for Laplacian" % time_taken_laplacian)

start_time_sobel = time.time()

sobel = use_sobel(img)

time_taken_sobel = time.time() - start_time_sobel
print("%.4f seconds for Sobel" % time_taken_sobel)

cv2.imshow('Original', img)
cv2.imshow('Canny Edge Detection', canny)
cv2.imshow('Laplacian Edge Detection', laplacian)
cv2.imshow('Sobel Edge Detection', sobel)

cv2.imwrite('canny-edge/canny_with_opencv.jpg', canny)
cv2.imwrite('canny-edge/laplacian_with_opencv.jpg', laplacian)
cv2.imwrite('canny-edge/sobel_with_opencv.jpg', sobel)

with open('canny-edge/time_taken_canny_with_opencv.txt', 'a') as f:
    f.write(str(time_taken_canny) + '\n')

with open('canny-edge/time_taken_laplacian_with_opencv.txt', 'a') as f:
    f.write(str(time_taken_laplacian) + '\n')

with open('canny-edge/time_taken_sobel_with_opencv.txt', 'a') as f:
    f.write(str(time_taken_sobel) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()