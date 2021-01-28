import cv2
import numpy as np

img = cv2.imread("pic3.jpg")
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 对图像进行二值化操作
# threshold(src, thresh, maxval, type, dst=None)
# src是输入数组，thresh是阈值的具体值，maxval是type取THRESH_BINARY或者THRESH_BINARY_INV时的最大值
# type有5种类型,这里取0： THRESH_BINARY ，当前点值大于阈值时，取maxval，也就是前一个参数，否则设为0
# 该函数第一个返回值是阈值的值，第二个是阈值化后的图像
ret, thresh = cv2.threshold(imggray, 127, 255, 0)
min_area = 5000

max_area = 200000

# findContours()有三个参数：输入图像，层次类型和轮廓逼近方法
# 该函数会修改原图像，建议使用img.copy()作为输入
# 由函数返回的层次树很重要，cv2.RETR_TREE会得到图像中轮廓的整体层次结构，以此来建立轮廓之间的‘关系’。
# 如果只想得到最外面的轮廓，可以使用cv2.RETE_EXTERNAL。这样可以消除轮廓中其他的轮廓，也就是最大的集合
# 该函数有三个返回值：修改后的图像，图像的轮廓，它们的层次
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

color = cv2.cvtColor(imggray, cv2.COLOR_GRAY2BGR)
for c in contours:

    area = cv2.contourArea(c)
    # if area>min_area and area <max_area:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(color,(x,y),(x+w, y + h), (36,255,12), 2)

# img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()