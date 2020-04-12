# -*- coding: utf-8 -*-
# coding by liuyunfei 
# 2020-4-12


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QObject, QMutexLocker, QMutex, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QPixmap, QImage
import os
import cv2
import time
import glob
import numpy as np
from copy import deepcopy

from ui.ui import *



image_mutex = QMutex()
image = None
org_img = None
camera_mutex = QMutex()
num_i = 0


def cv2img_to_Qpixmap(frame):
    if len(frame.shape) == 2:
        cvRGBImg = cv2.cvtColor(frame,cv2.COLOR_GRAY2RGB)
    elif len(frame.shape) == 3:
        cvRGBImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h,w,c = cvRGBImg.shape
    cvRGBImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    qimg = QImage(cvRGBImg.data, w, h, c*w, QImage.Format_RGB888)
    pixmap01 = QPixmap.fromImage(qimg)
    pix = QPixmap(pixmap01)
    return pix


class UpdateImg(QObject):
    update_pix1 = pyqtSignal(list)    
    def __init__(self):
        super(UpdateImg, self).__init__()
        self.image = None
    def run(self):
        fnames = glob.glob("imgs/*.png")
        allCorners = []
        allIds = []
        for name in fnames:
            im = cv2.imread(name,1)
            dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
            board = cv2.aruco.CharucoBoard_create(7, 9, .015, .0111, dictionary)  #0.025单位是米    
            corners, ids, rejected = cv2.aruco.detectMarkers(im, dictionary)
            print(len(corners))
            if corners == None or len(corners) == 0:
                continue
            ret, charucoCorners, charucoIds = cv2.aruco.interpolateCornersCharuco(corners, ids, im, board)  #其中的参数依赖于detectMarkers检测的初始值
            if corners is not  None  and charucoIds is not None:
                if len(corners) == 31:
                    allCorners.append(charucoCorners)
                    allIds.append(charucoIds)
            cv2.aruco.drawDetectedMarkers(im,corners,ids)             
            self.update_pix1.emit([im])
            time.sleep(0.1)
            
        w,h=im.shape[1],im.shape[0]
        ret, K, dist_coef, rvecs, tvecs = cv2.aruco.calibrateCameraCharuco(allCorners, allIds, board,(w,h),None,None)
        dist_coef = dist_coef[0]
        txt = "Matrix =\n {0}\nDist_coef =\n {1}\n{2}\n{3}\n{4}\n{5}\n\n- {6}".format(K,dist_coef[0],dist_coef[1],\
                                                                dist_coef[2],dist_coef[3],dist_coef[4],"By:Liu Yunfei")
        
        self.update_pix1.emit([None,txt])
        

class ColorImageThread(QObject):
    update_pix1 = pyqtSignal(list)   
    def __init__(self):
        super(ColorImageThread, self).__init__()        
    def run(self):
        global image
        global image_mutex
        while True:
            image_mutex.lock()
            img = deepcopy(image)
            image_mutex.unlock()
            if img is not None:
                self.update_pix1.emit([img])
            time.sleep(0.02)


class MyWindow(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.open_camera_button.clicked.connect(self.OnOpenCameraBtn)
        self.capture_button.clicked.connect(self.OnCaptureBtn)
        self.close_camera_button.clicked.connect(self.OnCloseCameraBtn)
        self.cali_button.clicked.connect(self.OnCaliBtn)
        self.set_button.clicked.connect(self.getSetInfo)
        self.image_label.setScaledContents(False)
        self.setWindowTitle("Camera Calibration using ChAruco by LiuYunfei")
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)

        self.camera_image = None  
        self.camera_no = 0
        self.camera_width = 0
        self.camera_height = 0
        self.aruco_width = 0
        self.aruco_height = 0      

        self.save_folder = ""
        self.cap = None
        self.sleep = False
        self.getSetInfo()
        

    def getSetInfo(self):
        camera_no = self.lineEdit1.text()
        camera_width = self.lineEdit2.text()
        camera_height = self.lineEdit3.text()
        aruco_width = self.lineEdit4.text()
        aruco_height = self.lineEdit5.text()

        self.camera_no = int(camera_no)
        self.camera_width = int(camera_width)
        self.camera_height = int(camera_height)
        self.aruco_width = int(aruco_width)
        self.aruco_height = int(aruco_height)
        
    def timerEvent(self):        
        global image
        global org_img
        global image_mutex
        if self.sleep ==False:
            time.sleep(2)
            self.sleep = True
        camera_mutex.lock()
        ret,frame = self.cap.read()
        camera_mutex.unlock()
        if ret:
            image_mutex.lock()
            org_img = deepcopy(frame)
            image_mutex.unlock()
            dd = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
            board = cv2.aruco.CharucoBoard_create(self.aruco_width, self.aruco_height, .015, .0111, dd)#0.025单位是米
            corners, ids, rejected = cv2.aruco.detectMarkers(frame,dd)            
            if corners == None or len(corners) == 0:
                pass
            else:                
                cv2.aruco.drawDetectedMarkers(frame,corners,ids)                        
            image_mutex.lock()
            image = deepcopy(frame)
            image_mutex.unlock()
            
    
    def updateColorImage(self,list_tmp):
        img = list_tmp[0]
        if img is not None:
            qimg = cv2img_to_Qpixmap(img)
            pix2 = qimg.scaled(800, 600, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.image_label.setPixmap(pix2)
        if len(list_tmp) > 1:
            text = list_tmp[1]
            self.label_result.setText(text)
    

    def OnOpenCameraBtn(self):
        self.cap = cv2.VideoCapture(self.camera_no)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        print("FPS = {} fps".format(fps))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,self.camera_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,self.camera_height)

        time.sleep(0.5)
        self.timer.start(30)

        self.updataImg = ColorImageThread()
        self.updataImg.update_pix1.connect(self.updateColorImage)
        self.uithread1 = QThread()
        self.updataImg.moveToThread(self.uithread1)
        self.uithread1.started.connect(self.updataImg.run)        
        self.uithread1.start()
        

    def OnCaliBtn(self):
        global image
        global image_mutex
        self.updateimg = UpdateImg()
        self.updateimg.update_pix1.connect(self.updateColorImage)
        self.ui2 = QThread()
        self.updateimg.moveToThread(self.ui2)
        self.ui2.started.connect(self.updateimg.run)
        self.ui2.start()
    
    def UpdateTimeUI(self,data):
        self.label_result.setText(data)        

    def OnCaptureBtn(self):        
        global image
        global image_mutex
        global org_img
        global num_i
        image_mutex.lock()
        img =  deepcopy(org_img)
        image_mutex.unlock()
        name = "imgs/{}.png".format(num_i)
        cv2.imwrite(name,img)
        print("({}),img saved. {}".format(num_i,name))
        num_i +=1

    def OnCloseCameraBtn(self):
        self.timer.stop()        
        self.updataImg.disconnect()
        #self.updataImg.update_pix1.disconnect()
        self.uithread1.terminate()
        camera_mutex.lock()
        self.cap.release()
        camera_mutex.unlock()
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())


