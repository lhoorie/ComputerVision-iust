import cv2
import os
import numpy as np
import glob

#Q4_1
path1 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images\img1.png'
image1 = cv2.imread(path1)
cv2.imshow('image1', image1)
cv2.waitKey(0)

#Q4_2
flags = cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE
found, corners = cv2.findChessboardCorners(image1, (24, 17))
# print(corners)

#Q4_3
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
corners2 = cv2.cornerSubPix(gray_image1,corners,(5,5),(-1,-1),criteria)
image2 = cv2.drawChessboardCorners(image1, (24,17), corners2, found)
path2 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images'
cv2.imwrite(os.path.join(path2, 'mypic.jpg') , image2)
cv2.imshow('image2', image2)
cv2.waitKey(0)

#Q4_4 https://www.programcreek.com/python/example/89320/cv2.calibrateCamera
objpoints = []
imgpoints = []
objp = np.zeros((24 * 17, 3), np.float32)
objp[:, :2] = np.mgrid[0:24, 0:17].T.reshape(-1, 2)
objpoints.append(objp)
imgpoints.append(corners2)
img_size = (image1.shape[1], image1.shape[0])
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)
print('ret:', ret)
print('\n*****************************************')
print('\nmtx:', mtx)
print('\n*****************************************')
print('\ndist:', dist)
print('\n*****************************************')
print('\nrvecs:', rvecs)
print('\n*****************************************')
print('\ntvecs:', tvecs)

#Q4_5
print('\nk1:', dist[0][0])
print('\nk2:', dist[0][1])
print('\np1:', dist[0][2])
print('\np2:', dist[0][3])
print('\nk3:', dist[0][4])

#Q4_6 https://medium.com/@elifozcakiir/camera-calibration-with-opencv-9fb104fdf879
x, y = image1.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(x,y),0,(x,y))
path3 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images\img5.png'
image5 = cv2.imread(path3)
dst = cv2.undistort(image5, mtx, dist, None, newcameramtx)
cv2.imwrite(os.path.join(path2, 'undistort.jpg') , dst)

#Q4_7
objpoints = []
imgpoints = []
img_size = []
def undistort(p, nx, ny):
    img = cv2.imread(p)
    objp = np.zeros((nx * ny, 3), np.float32)
    objp[:, :2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)
    found, corners = cv2.findChessboardCorners(img, (nx, ny))
    if found:
        objpoints.append(objp)
        imgpoints.append(corners)
        img_size.append((img.shape[1], img.shape[0]))

path_img1 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images\img1.png'
path_img2 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images\img2.png'
path_img3 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images\img3.png'
path_img4 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images\img4.png'

undistort(path_img1, 24, 17)
undistort(path_img2, 17, 24)
undistort(path_img3, 24, 17)
undistort(path_img4, 24, 17)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size[0], None, None)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,img_size[0],0,img_size[0])
path_img5 = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images\img5.png'
path_images = r'D:\iust stuff\4011\FCV\homeworks\HW[2]\images'
image5 = cv2.imread(path_img5)
dst = cv2.undistort(image5, mtx, dist, None, newcameramtx)
cv2.imwrite(os.path.join(path_images, 'undistort[1-4].jpg') , dst)
