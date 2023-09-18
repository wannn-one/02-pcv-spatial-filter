# gaussian blur with opencv

import cv2
import time
import numpy as np
import os

if not os.path.exists('lpf-filter'):
    os.makedirs('lpf-filter')

# Membaca File Citra
start_time = time.time()

f = cv2.imread("images/a.jpg",cv2.IMREAD_GRAYSCALE)
g3 = cv2.GaussianBlur(f,(3,3),0)

time_taken = time.time() - start_time
print("%.4f seconds" % time_taken)

cv2.imshow('Citra Asli', f)
cv2.imshow('Hasil Gaussian Kernel 3x3', g3)

cv2.imwrite('lpf-gaussian/lpf-gaussian_gaussian_with_opencv.jpg', g3)
with open('lpf-gaussian/time_taken_lpf-gaussian_gaussian_with_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()