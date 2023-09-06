import cv2
img=cv2.imread('lena.jpg',0)
cv2.imshow("Image",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()