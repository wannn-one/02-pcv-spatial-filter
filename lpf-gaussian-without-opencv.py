import cv2
import time
import numpy as np 
import os

if not os.path.exists('lpf-filter'):
    os.makedirs('lpf-filter')

def Convolosi(f,w):
    baris = f.shape[0]
    kolom = f.shape[1]
    dkernel = w.shape[0]
    dkernel2= np.int32(np.floor(dkernel/2)) 

    g =np.zeros((baris,kolom))
    for y in range(baris):
        for x in range(kolom):
            g[y,x] = 0 
            for i in range(dkernel):
                yy =y+i-dkernel2
                if (yy<0)|(yy>=baris-1):
                    continue 
                for j in range(dkernel):
                    xx =x+j - dkernel2
                    if (xx<0)|(xx>=kolom-1): 
                        continue 
                    g[y,x]=g[y,x]+f[yy,xx]*w[i,j]

    g= np.uint8(np.floor(g))
    return g

# Membaca File Citra
start_time = time.time()

f = cv2.imread("images/a.jpg",cv2.IMREAD_GRAYSCALE)

w = np.array([[0.3679,0.6065,0.3679],[0.6065,1.0000,0.6065],[0.3679,0.6065,0.3679]])/4.8976
g3 = Convolosi(f,w)

time_taken = time.time() - start_time
print("%.4f seconds" % time_taken)

cv2.imshow('Citra Asli', f)
cv2.imshow('Hasil Gaussian Kernel 3x3', g3)

cv2.imwrite('lpf-gaussian/lpf-gaussian_gaussian_without_opencv.jpg', g3)
with open('lpf-gaussian/time_taken_lpf-gaussian_gaussian_without_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()