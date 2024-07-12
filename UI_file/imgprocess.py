#######################
#左上：7            水平翻转
#上：1              不变
# 右上：6           不变
# 右边：2           不变
# 右下：4           垂直翻转
# 下：0             不变
# 左下：5           垂直翻转
# 左：3             水平翻转
import os
import cv2
import numpy as np

sorce_path = "D:\PlasticFrame\img\摄像机拍照方式"
sub_path = ["\\0","\\1","\\2","\\3","\\4","\\5","\\6","\\7"]
main_path = []
Sum_path = [[] for _ in range(8)] 

for i in range(8):
    try:
        # 取得带"0/1/2"的路径
        main_path = sorce_path + sub_path[i]
        # print(main_path)

        #取得文件夹下图片的名字
        file_name = os.listdir(main_path)
        for item in file_name:
            # 检查文件扩展名，这里假设图片文件的扩展名为.jpg或.png
            if item.lower().endswith(('.jpg', '.png')):
                #取得所有照片的绝对路径
                absolute_path = os.path.join(main_path, item)
                Sum_path[i].append(absolute_path)
    except Exception as e:
        print(f"处理路径 {main_path} 时发生错误: {e}")

# for i in range(len(Sum_path[0])):
i = 0
img_path = Sum_path[0][i]
img = cv2.imread(img_path)

#灰度化
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
_,threshold_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
#检测轮廓
contours,_ = cv2.findContours(threshold_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow(gray_image)
cv2.imshow(threshold_image)


                