# 02-spatial-filter

A Task for Image & Video Processing Course, comparing spatial convolution, lowpass spatial filter, lowpass with gaussian kernel, 1D highpass spatial filter, and 2D highpass spatial filter with and without OpenCV

## Feature

1. Measure time taken for each method to perform spatial convolution, lowpass spatial filter, lowpass with gaussian kernel, 1D highpass spatial filter, and 2D highpass spatial filter
2. Compare the result of each method
3. Compare the time taken for each method

## Prequisites

```
python3
opencv
numpy
```

## Program usage

`hpf-without-opencv.py` is a program to perform 1D highpass spatial filter without using OpenCV

`hpf-with-opencv.py` is a program to perform 2D highpass spatial filter using OpenCV

`lpf-without-opencv.py` is a program to perform lowpass spatial filter without using OpenCV

`lpf-with-opencv.py` is a program to perform lowpass spatial filter using OpenCV

`conv-2d-with-opencv.py` is a program to perform 2d convolution using OpenCV

`conv-2d-without-opencv.py` is a program to perform 2d convolution without using OpenCV

`lpf-gaussian-with-opencv.py` is a program to perform lowpass spatial filter with gaussian kernel using OpenCV

`lpf-gaussian-without-opencv.py` is a program to perform lowpass spatial filter with gaussian kernel without using OpenCV

`combine.py` is a program to get every hpf-edge images (laplacial, sobel, canny) and combine them into one image

Coming soon

## How to use?

Install all the prequisites.

```
pip install -r requirements.txt
```

Simply type in your terminal:

```
python3 <the-program-to-use>.py
```