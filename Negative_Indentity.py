import cv2
# img = cv2.imread('yash.jpg')
# cv2.imshow('My image',img)
i=1
while i<11:
    img = cv2.imread(f'{i}.jpg')
    cv2.imshow(f'My image{i}',img)
    negative = 255-img 
    cv2.imshow(f'Negative{i}',negative)
    i=i+1
cv2.waitKey(5500)
cv2.destroyAllWindows()
# negative2 = 255-img2
# cv2.imshow('NegativeTwo',negative2)
# while i<=10:
# first we need to download this library in our system to run cv commmand
#  pip install opencv-python
# linear 
# logarithametic = identity and negative
# power
