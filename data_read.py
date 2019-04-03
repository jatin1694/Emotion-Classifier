import numpy as np
import cv2

# Read the start pic for subject 1
start_s1 = cv2.imread("image/data/S005/001/S005_001_00000001.png", 0)

# Read the end pic for subject 2
end_s1 = cv2.imread("image/data/S005/001/S005_001_00000011.png", 0)

# print the shape for the image data
print(start_s1.shape)
print(end_s1.shape)

#calculates the difference between start and end pixels
print(np.subtract(end_s1, start_s1))

#Shows both the images in open CV window
cv2.imshow("start", start_s1)
cv2.imshow("end", end_s1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Read the start pic for subject 1
start_s2 = cv2.imread("image/data/S010/001/S010_001_00000001.png", 0)

#Read the start pic for subject 2
end_s2 = cv2.imread("image/data/S010/001/S010_001_00000014.png", 0)

print("Printing subject 1 difference")
print(np.subtract(end_s2, start_s2))


cv2.imshow("start", start_s1)
cv2.imshow("end", end_s1)

cv2.imshow("start", start_s2)
cv2.imshow("end", end_s2)
cv2.waitKey(0)
cv2.destroyAllWindows()