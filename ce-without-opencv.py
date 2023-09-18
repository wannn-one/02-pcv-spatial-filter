import cv2
import numpy as np
import time
import os

if not os.path.exists('canny-edge'):
    os.makedirs('canny-edge')

def Convolosi(f,w):
    f  =np.float64(f)/255 
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
    
    return g

# Membaca File Citra
f = cv2.imread("images/a.jpg",cv2.IMREAD_GRAYSCALE)

start_time = time.time()

w = np.array([[0,1,0],[1,-4.,1],[0,1,0]])
g = Convolosi(f,w)

time_taken = time.time() - start_time
print("%.4f seconds" % time_taken)

cv2.imshow('Citra Asli', f)
cv2.imshow('Highpass Filter', g)

cv2.imwrite('canny-edge/canny_edge_without_opencv.jpg', g)
with open('canny-edge/time_taken_canny_edge_without_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()