import cv2

cam = cv2.VideoCapture(1)
ret, img = cam.read()
ret, img = cam.read()
print(ret)
print(img.shape, img.dtype)
cv2.imwrite("Camerafeed.png", img) 

cam.release()
