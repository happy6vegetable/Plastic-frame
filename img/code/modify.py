import cv2,os
import numpy as np


path = "../database/0"
datanames = os.listdir(path)


for obj in datanames:
    filename = path +'/'+ obj
    image = cv2.imread(filename)
    gauss = cv2.GaussianBlur(image,(5,5),0)     ##进行高斯滤波
    median = cv2.medianBlur(image,5)            ##进行中值滤波

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)    ##转化为灰度图
    corners = cv2.goodFeaturesToTrack(gray,50,0.1,10)  ##获取图像特征点

    laplacian = cv2.Laplacian(gray,cv2.CV_64F)          #拉普拉斯算法给出图像变化的趋势
    canny = cv2.Canny(gray,100,200)                     #梯度算法，用于检测边缘

    ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)   #图像的二值化
    binary_adaptive = cv2.adaptiveThreshold(            #自适应阈值算法
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)   
    ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)    #自动分析阈值的算法

    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(binary, kernel)             #腐蚀边缘
    dilation = cv2.dilate(binary, kernel)           #膨胀边缘

    erosion_name = './result/' + 'erosion_' + obj
    cv2.imwrite(erosion_name,erosion)                       
    dilation_name = './result/' + 'dilation_' + obj
    cv2.imwrite(dilation_name,dilation)


    binary_name = './result/' + 'binary_' + obj
    cv2.imwrite(binary_name,binary)
    adaptive_name = './result/' + 'adaptive_' + obj
    cv2.imwrite(adaptive_name,binary_adaptive)
    otsu_name = './result/' + 'otsu_' + obj
    cv2.imwrite(otsu_name,binary_otsu)

    gray_name = './result/' + 'gray_' + obj
    cv2.imwrite(gray_name,gray)

    laplacian_name = './result/' + 'laplacian_' + obj
    cv2.imwrite(laplacian_name,laplacian)

    canny_name = './result/' + 'canny_' + obj
    cv2.imwrite(canny_name,canny)


    gauss_name = './result/' + 'gauss_' + obj
    median_name = './result/' + 'median_' + obj
    cv2.imwrite(gauss_name,gauss)
    cv2.imwrite(median_name,gauss)

    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(image,(int(x),int(y)),3,(255,0,255),-1)

    circle_name = './result/' + 'circle_' + obj
    cv2.imwrite(circle_name,image)
    

