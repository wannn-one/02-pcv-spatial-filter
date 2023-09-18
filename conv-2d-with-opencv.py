import cv2
import numpy as np
import os
import time

# convolution 2d with opencv
if not os.path.exists('conv-2d'):
    os.makedirs('conv-2d')

kernel_number = 3 # ukuran kernel 3x3, bisa diubah sesuai kebutuhan

# read image
img = cv2.imread('images/a.jpg', cv2.IMREAD_GRAYSCALE)

for i in range(10): # stress test
    start_time = time.time()

# create kernel
    kernel = np.ones((kernel_number,kernel_number), np.float32)/kernel_number**2

# apply kernel
    dst = cv2.filter2D(img, -1, kernel) # -1 means the depth of the output image is the same as the input image

    time_taken = time.time() - start_time
    print("%.4f seconds" % time_taken)
    with open('conv-2d/time_taken_conv2d_with_opencv.txt', 'a') as f:
        f.write(str(time_taken) + '\n')

# show image
cv2.imshow('Original', img)
cv2.imshow('Convolution 2D', dst)

cv2.imwrite('conv-2d/conv2d_with_opencv.jpg', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()