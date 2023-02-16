import cv2
import os

# Q4_2
path1 = r'D:\iust stuff\4011\FCV\HW[1]\background.png'
image1 = cv2.imread(path1)
cv2.imshow('image1', image1)
cv2.waitKey(0)

# Q4_3
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
cv2.imshow('image2', image2)
cv2.waitKey(0)

# Q4_4
image3 = cv2.resize(image1, (570, 290))
cv2.imshow('image3', image3)
cv2.waitKey(0)

# Q4_5
line1 = cv2.line(image1, (0,0), (560, 0), (255, 0, 0), 5)
line2 = cv2.line(line1, (560,0), (560, 280), (255, 0, 0), 5)
line3 = cv2.line(line2, (560,280), (0, 280), (255, 0, 0), 5)
line4 = cv2.line(line3, (0,280), (0, 0), (255, 0, 0), 5)
cv2.imshow('image4', line4)
cv2.waitKey(0)

# Q4_6
cir1 = cv2.circle(line4, (0,0), 10, (0, 200, 0), 2)
cir2 = cv2.circle(cir1, (0,280), 10, (0, 100, 100), 2)
cir3 = cv2.circle(cir2, (560,0), 10, (0, 0, 200), 2)
cir4 = cv2.circle(cir3, (560,280), 10, (100, 100, 0), 2)
cv2.imshow('image5', cir4)
cv2.waitKey(0)

# Q4_7
l1 = cv2.line(cir4, (0,0), (80, 140), (255, 0, 0), 1)
l2 = cv2.line(l1, (0,0), (160, 140), (255, 0, 0), 1)
l3 = cv2.line(l2, (0,0), (240, 140), (255, 0, 0), 1)
l4 = cv2.line(l3, (0,0), (320, 140), (255, 0, 0), 1)
l5 = cv2.line(l4, (0,0), (400, 140), (255, 0, 0), 1)
l6 = cv2.line(l5, (0,0), (480, 140), (255, 0, 0), 1)
l7 = cv2.line(l5, (0,0), (560, 140), (255, 0, 0), 1)

l8 = cv2.line(l7, (560,0), (80, 140), (255, 0, 0), 1)
l9 = cv2.line(l8, (560,0), (160, 140), (255, 0, 0), 1)
l10 = cv2.line(l9, (560,0), (240, 140), (255, 0, 0), 1)
l11 = cv2.line(l10, (560,0), (320, 140), (255, 0, 0), 1)
l12 = cv2.line(l11, (560,0), (400, 140), (255, 0, 0), 1)
l13 = cv2.line(l12, (560,0), (480, 140), (255, 0, 0), 1)
l14 = cv2.line(l13, (560,0), (560, 140), (255, 0, 0), 1)

l15 = cv2.line(l14, (560,280), (80, 140), (255, 0, 0), 1)
l16 = cv2.line(l15, (560,280), (160, 140), (255, 0, 0), 1)
l17 = cv2.line(l16, (560,280), (240, 140), (255, 0, 0), 1)
l18 = cv2.line(l17, (560,280), (320, 140), (255, 0, 0), 1)
l19 = cv2.line(l18, (560,280), (400, 140), (255, 0, 0), 1)
l20 = cv2.line(l19, (560,280), (480, 140), (255, 0, 0), 1)
l21 = cv2.line(l20, (560,280), (560, 140), (255, 0, 0), 1)

l22 = cv2.line(l21, (0,280), (80, 140), (255, 0, 0), 1)
l23 = cv2.line(l22, (0,280), (160, 140), (255, 0, 0), 1)
l24 = cv2.line(l23, (0,280), (240, 140), (255, 0, 0), 1)
l25 = cv2.line(l24, (0,280), (320, 140), (255, 0, 0), 1)
l26 = cv2.line(l25, (0,280), (400, 140), (255, 0, 0), 1)
l27 = cv2.line(l26, (0,280), (480, 140), (255, 0, 0), 1)
l28 = cv2.line(l27, (0,280), (560, 140), (255, 0, 0), 1)
l29 = cv2.line(l28, (560,280), (0, 140), (255, 0, 0), 1)
l30 = cv2.line(l29, (560,0), (0, 140), (255, 0, 0), 1)

cv2.imshow('image6', l30)
cv2.waitKey(0)

# Q4_8
path2 = r'D:\iust stuff\4011\FCV\HW[1]'
f = cv2.imwrite(os.path.join(path2, 'mypic.jpg') , l30)
print(f)
