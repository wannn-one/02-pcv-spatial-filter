import cv2
import numpy as np

# Baca dua gambar
image1 = cv2.imread('hpf-edge/canny_with_opencv.jpg')
image2 = cv2.imread('hpf-edge/laplacian_with_opencv.jpg')
image3 = cv2.imread('hpf-edge/sobel_with_opencv.jpg')

# Pastikan kedua gambar memiliki ukuran yang sama
# Jika tidak, Anda mungkin perlu mengubah ukuran salah satu gambar untuk membuatnya cocok
# image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Gabungkan kedua gambar menjadi satu citra besar
comb_img = np.hstack((image1, image2, image3))

# Tampilkan citra gabungan dalam satu jendela
cv2.imshow('Combined Image', comb_img)
cv2.imwrite('hpf-edge/combined_image.jpg', comb_img)
# Tunggu sampai pengguna menekan tombol apa pun
cv2.waitKey(0)
cv2.destroyAllWindows()
