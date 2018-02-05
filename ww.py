# -*- coding: utf-8 -*-
import cv2
import sys

import time
from PIL import Image

def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)

    cap = cv2.VideoCapture(camera_idx)
    #人脸识别分类器
    classfier = cv2.CascadeClassifier(r"D:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml")

    # 识别出人脸后，圈的边框的颜色
    color = (0,0,200)

    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# 将当前帧转换成灰度图像

        # 开始人脸检测
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
        if len(faceRects) > 0:  # 大于0,则检测到人脸
            for faceRect in faceRects:  # 框出每一张人脸
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 15, y - 15), (x + w + 15, y + h + 15), color, 2)

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    cap.release()# 释放摄像头
    cv2.destroyAllWindows()


if __name__ == '__main__':
    f =open('D:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml', 'r')
    #if len(sys.argv) != 2:
     #   print("Usage:%s camera_id\r\n" % (sys.argv[0]))
    #else:
    CatchUsbVideo("Hello Man", 0)
    time.wait(10)
   # cv2.destroyAllWindows()