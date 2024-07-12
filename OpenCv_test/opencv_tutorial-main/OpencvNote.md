## 图像的载入、显示和保存

```
import cv2

# 载入一张图像
img = cv2.imread('image.jpg')

# 显示图像
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 显示不同的灰度：

```
cv2.imshow("blow",image[:,:,0])
cv2.imshow("green", image[:, :, 1])
cv2.imshow("red", image[:, :, 2])

```


# 保存图像
cv2.imwrite('new_image.jpg', img)

```

## 获取和修改像素值

```
# 获取和修改像素值
px = img[100,100]
print(px)

# 修改像素值
img[100,100] = [255,255,255]
print(img[100,100])

```

## 获取图像的基本属性（如大小、通道数、像素数等）

```
# 获取图像属性
print(img.shape)
print(img.size)
print(img.dtype)
```

## 拆分和合并图像通道

```
# 拆分和合并图像通道
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

```

## 图像色彩空间的转换

```

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

```

## 图像阈值化

```
# 阈值化处理
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

```
## 图像的裁剪

```
crop = image[10:170, 40:200]

```

## 图形的绘制

```
# 创建一个画布
image = np.zeros([300, 300, 3], dtype=np.uint8)

# 画一个线段
cv2.line(image, (100, 200), (250, 250), (255, 0, 0), 2)
# 画一个矩形框
cv2.rectangle(image, (30, 100), (60, 150), (0, 255, 0), 2)
# 画一个圆环
cv2.circle(image, (150, 100), 20, (0, 0, 255), 3)
# 绘制字符串
cv2.putText(image, "hello", (100, 50), 0, 1, (255, 255, 255), 2, 1)

```
## 均值滤波

### 高斯滤波

**概念** 

高斯滤波(Gaussian filter) 包含许多种，包括低通、带通和高通等，我们通常图像上说的高斯滤波，指的是 高斯模糊(Gaussian Blur) ，是一种 高斯低通滤波 ，其过滤调图像高频成分（图像细节部分），保留图像低频成分（图像平滑区域），所以对图像进行 ‘高斯模糊’ 后，图像会变得模糊。

高斯模糊对于抑制 高斯噪声 (服从正态分布的噪声) 非常有效。

[【图像处理】之高斯滤波：原理、代码实现和优化加速_高斯滤波可以用于优化电流信号吗-CSDN博客](https://blog.csdn.net/a435262767/article/details/107115249)

### 中值滤波

**概念** 
中值滤波是一种非线性的信号处理方法，所以它是一种非线性滤波器，也是一种统计排序滤波器。它将每一像素点的灰度值设置为该点某邻域窗口内的所有像素点灰度值的中值。
**目的**
中值滤波对孤立的噪声像素即椒盐噪声、脉冲噪声具有良好的滤波效果，可以保持图像的边缘特性，不会使图像产生显著的模糊

```
# 高斯滤波
gauss = cv2.GaussianBlur(image, (5, 5), 0)
# 中值滤波
median = cv2.medianBlur(image, 5)

```
## 图像特征的提取


```
image = cv2.imread("opencv_logo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)


```
## 模板匹配

```
template = gray[75:105, 235:265]

match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

```



