
import cv2
image=cv2.imread("lena.jpg",1)
w,h,_=image.shape
cv2.circle(image,(20,20),20,(0,0,255),-1)
cv2.circle(image,(w - 20,20),20,(0,0,255),-1)
cv2.circle(image,(20,h - 20),20,(0,0,255),-1)
cv2.circle(image,(w - 20,h - 20),20,(0,0,255),-1)
cv2.rectangle(image,(200,300),(300,250),(0,255,0),4)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"hello",(210,290),font,1,(10,56,167),2)

cv2.line(image,(0,0),(600,600),(255,0,0),5)



cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()