import cv2
import numpy as np
import time
import os

if not os.path.exists('conv-2d'):
    os.makedirs('conv-2d')

kernel_number = 3 # ukuran kernel 3x3, bisa diubah sesuai kebutuhan

def Convolusi(f,w):
    baris = f.shape[0]
    kolom = f.shape[1]
    g = np.zeros((baris,kolom))
    for y in range(baris):
        for x in range(kolom):
            g[y,x] = 0 
            for i in range(kernel_number):
                yy = y+i-1
                if (yy < 0) or (yy>=baris-1):
                    continue 
                for j in range(kernel_number):
                    xx = x+j - 1
                    if (xx<0) or (xx>=kolom-1): 
                        continue 
                    g[y,x]=g[y,x]+f[yy,xx]*w[i,j]
                #end for
            #end for 
        #end for
    #end for
    g = np.uint8(np.floor(g))
    return g
# Membaca File Citra
f = cv2.imread("images/a.jpg",cv2.IMREAD_GRAYSCALE)

start_time = time.time()

w =np.ones((kernel_number,kernel_number))/kernel_number**2

#   |1/9 1/9 1/9 | 
#w =|1/9 1/9 1/9 |
#   |1/9 1/9 1/9 | 
    
g = Convolusi( f,w)

time_taken = time.time() - start_time
print("%.4f seconds" % time_taken)

cv2.imshow('Original', f)
cv2.imshow('Convolution 2D', g)

cv2.imwrite('conv-2d/conv2d_without_opencv.jpg', g)
with open('conv-2d/time_taken_conv2d_without_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()