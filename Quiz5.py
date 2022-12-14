import cv2 as cv
import numpy as np
# import matplotlib as plt

lenaIMG = cv.imread('lena.png', cv.IMREAD_GRAYSCALE)
imArray = np.asarray(lenaIMG)
cv.imshow("Lena",imArray)
cv.waitKey(0)

# Display Shape of Numpy Array

print ("Shape of Image is ", imArray.shape)

# Image Slicing

imSlice = imArray[200:300,200:300]
cv.imshow("Lena Slice",imSlice)
cv.waitKey(0)


# Transpose of a Image results in 90 degrees Rotation

imArrayT = imArray.T
cv.imshow("Lena Transpose",imArrayT)
cv.waitKey(0)

# Reshaped Image to 64 x 64 x 64

imArrayReshaped = imArray.reshape(64,64,64)
print ("Reshaped Image Shape is ",imArrayReshaped.shape)

moon = cv.imread('moon.png', cv.IMREAD_GRAYSCALE)
moonArray = np.asarray(moon)
moonArray = moonArray[0:512,0:512]

# Add two images

sumIm = moonArray + imArray

cv.imshow("Sum Image",sumIm)
cv.waitKey(0)

# Subtract Two Images

difIm = imArray - moonArray
cv.imshow("Diff Image",difIm)
cv.waitKey(0)


