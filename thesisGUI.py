import sys
import threading
import time
from time import sleep
import Queue
import numpy as np
import serial

import UARTCommand
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

BAP_QUEUE_SIZE = 1

BAP_RecvMsgQueue = Queue.Queue(BAP_QUEUE_SIZE)

BAP_SendMsgQueue = Queue.Queue(BAP_QUEUE_SIZE)
BAP_SendMsgQueueMutex = threading.Lock()
BAP_SendMsgQueueSem = threading.Semaphore(1)

BAP_SharedVarsMutex = threading.Lock()

BAP_SharedVarsList = [None]*10

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Ui_MainWindow(object):
    def __init__(self, window, recvmsg):
        self.window = window
        self.recvmsg = recvmsg
        self.setupUi(window)
        self.Running = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 720)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Plate_Controller_Fr = QtWidgets.QFrame(self.centralWidget)
        self.Plate_Controller_Fr.setGeometry(QtCore.QRect(10, 10, 311, 211))
        self.Plate_Controller_Fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Plate_Controller_Fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Plate_Controller_Fr.setObjectName("Plate_Controller_Fr")
        self.Plate_Controller_La = QtWidgets.QLabel(self.Plate_Controller_Fr)
        self.Plate_Controller_La.setGeometry(QtCore.QRect(10, 0, 101, 21))
        self.Plate_Controller_La.setObjectName("Plate_Controller_La")
        self.Plate_Controller_Apply_Bu = QtWidgets.QPushButton(self.Plate_Controller_Fr)
        self.Plate_Controller_Apply_Bu.setGeometry(QtCore.QRect(22, 170, 271, 32))
        self.Plate_Controller_Apply_Bu.setObjectName("Plate_Controller_Apply_Bu")
#Add button callback
        self.Plate_Controller_Apply_Bu.clicked.connect(self.BAP_Controller_Apply)
####################
        self.Plate_Controller_PID_GB = QtWidgets.QGroupBox(self.Plate_Controller_Fr)
        self.Plate_Controller_PID_GB.setGeometry(QtCore.QRect(20, 40, 121, 131))
        self.Plate_Controller_PID_GB.setObjectName("Plate_Controller_PID_GB")
        self.PID_Kd_Box = QtWidgets.QDoubleSpinBox(self.Plate_Controller_PID_GB)
        self.PID_Kd_Box.setGeometry(QtCore.QRect(30, 90, 81, 24))
        self.PID_Kd_Box.setDecimals(4)
#Max-Min
        self.PID_Kd_Box.setMinimum(0)
        self.PID_Kd_Box.setMaximum(9.99)
###################
        self.PID_Kd_Box.setSingleStep(0.1)
        self.PID_Kd_Box.setObjectName("PID_Kd_Box")
        self.PID_Kp_La = QtWidgets.QLabel(self.Plate_Controller_PID_GB)
        self.PID_Kp_La.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.PID_Kp_La.setLineWidth(2)
        self.PID_Kp_La.setObjectName("PID_Kp_La")
        self.PID_Kd_La = QtWidgets.QLabel(self.Plate_Controller_PID_GB)
        self.PID_Kd_La.setGeometry(QtCore.QRect(10, 90, 21, 16))
        self.PID_Kd_La.setLineWidth(2)
        self.PID_Kd_La.setObjectName("PID_Kd_La")
        self.PID_Ki_Box = QtWidgets.QDoubleSpinBox(self.Plate_Controller_PID_GB)
        self.PID_Ki_Box.setGeometry(QtCore.QRect(30, 60, 81, 24))
        self.PID_Ki_Box.setDecimals(4)
#Max-Min
        self.PID_Ki_Box.setMinimum(0)
        self.PID_Ki_Box.setMaximum(9.99)
#####################
        self.PID_Ki_Box.setSingleStep(0.1)
        self.PID_Ki_Box.setObjectName("PID_Ki_Box")
        self.PID_Kp_Box = QtWidgets.QDoubleSpinBox(self.Plate_Controller_PID_GB)
        self.PID_Kp_Box.setGeometry(QtCore.QRect(30, 30, 81, 24))
        self.PID_Kp_Box.setDecimals(4)
#Max-Min
        self.PID_Kp_Box.setMinimum(0)
        self.PID_Kp_Box.setMaximum(9.99)
####################
        self.PID_Kp_Box.setSingleStep(0.1)
        self.PID_Kp_Box.setObjectName("PID_Kp_Box")
#Init value
        self.PID_Kp_Box.setValue(0.05)
        self.PID_Ki_Box.setValue(0)
        self.PID_Kd_Box.setValue(0.03)
###################
        self.PID_Ki_La = QtWidgets.QLabel(self.Plate_Controller_PID_GB)
        self.PID_Ki_La.setGeometry(QtCore.QRect(10, 60, 21, 16))
        self.PID_Ki_La.setLineWidth(2)
        self.PID_Ki_La.setObjectName("PID_Ki_La")
        self.Plate_Controller_SMC_GB = QtWidgets.QGroupBox(self.Plate_Controller_Fr)
        self.Plate_Controller_SMC_GB.setGeometry(QtCore.QRect(170, 40, 121, 101))
        self.Plate_Controller_SMC_GB.setObjectName("Plate_Controller_SMC_GB")
        self.SMC_k1_Box = QtWidgets.QDoubleSpinBox(self.Plate_Controller_SMC_GB)
        self.SMC_k1_Box.setGeometry(QtCore.QRect(30, 60, 81, 24))
        self.SMC_k1_Box.setDecimals(4)
#Max-Min
        self.SMC_k1_Box.setMinimum(0)
        self.SMC_k1_Box.setMaximum(9.99)
###################
        self.SMC_k1_Box.setSingleStep(0.1)
        self.SMC_k1_Box.setObjectName("SMC_k1_Box")
        self.SMC_K_Box = QtWidgets.QDoubleSpinBox(self.Plate_Controller_SMC_GB)
        self.SMC_K_Box.setGeometry(QtCore.QRect(30, 30, 81, 24))
        self.SMC_K_Box.setDecimals(4)
#Max-Min
        self.SMC_K_Box.setMinimum(0)
        self.SMC_K_Box.setMaximum(9.99)
###################
        self.SMC_K_Box.setSingleStep(0.1)
        self.SMC_K_Box.setObjectName("SMC_K_Box")
#Init value
        self.SMC_K_Box.setValue(3)
        self.SMC_k1_Box.setValue(2.5)
###################
#Disable K and K1 box by default
        self.SMC_K_Box.lineEdit().setEnabled(False)
        self.SMC_k1_Box.lineEdit().setEnabled(False) 
################################
        self.SMC_k1_La = QtWidgets.QLabel(self.Plate_Controller_SMC_GB)
        self.SMC_k1_La.setGeometry(QtCore.QRect(10, 60, 21, 16))
        self.SMC_k1_La.setLineWidth(2)
        self.SMC_k1_La.setObjectName("SMC_k1_La")
        self.SMC_K_La = QtWidgets.QLabel(self.Plate_Controller_SMC_GB)
        self.SMC_K_La.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.SMC_K_La.setLineWidth(2)
        self.SMC_K_La.setObjectName("SMC_K_La")
        self.Plate_Controller_PID_Ch = QtWidgets.QRadioButton(self.Plate_Controller_Fr)
        self.Plate_Controller_PID_Ch.setGeometry(QtCore.QRect(20, 20, 51, 20))
        self.Plate_Controller_PID_Ch.setObjectName("Plate_Controller_PID_Ch")
#Checked by default
        self.Plate_Controller_PID_Ch.toggled.connect(self.BAP_Controller_PID_Toggle)
        self.Plate_Controller_PID_Ch.setChecked(True)
###################
        self.Plate_Controller_SMC_Ch = QtWidgets.QRadioButton(self.Plate_Controller_Fr)
        self.Plate_Controller_SMC_Ch.setGeometry(QtCore.QRect(170, 20, 51, 20))
        self.Plate_Controller_SMC_Ch.setObjectName("Plate_Controller_SMC_Ch")
#Unchecked by default
        self.Plate_Controller_SMC_Ch.toggled.connect(self.BAP_Controller_SMC_Toggle)
        self.Plate_Controller_SMC_Ch.setChecked(False)
###################
        self.Mode_Fr = QtWidgets.QFrame(self.centralWidget)
        self.Mode_Fr.setGeometry(QtCore.QRect(9, 240, 311, 381))
        self.Mode_Fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mode_Fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mode_Fr.setObjectName("Mode_Fr")
        self.Mode_La = QtWidgets.QLabel(self.Mode_Fr)
        self.Mode_La.setGeometry(QtCore.QRect(10, 0, 101, 21))
        self.Mode_La.setObjectName("Mode_La")
        self.Mode_Circle_GB = QtWidgets.QGroupBox(self.Mode_Fr)
        self.Mode_Circle_GB.setGeometry(QtCore.QRect(10, 40, 291, 91))
        self.Mode_Circle_GB.setObjectName("Mode_Circle_GB")
        self.Circle_R_La = QtWidgets.QLabel(self.Mode_Circle_GB)
        self.Circle_R_La.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.Circle_R_La.setLineWidth(2)
        self.Circle_R_La.setObjectName("Circle_R_La")
        self.Circle_CentralY_La = QtWidgets.QLabel(self.Mode_Circle_GB)
        self.Circle_CentralY_La.setGeometry(QtCore.QRect(190, 30, 61, 16))
        self.Circle_CentralY_La.setLineWidth(2)
        self.Circle_CentralY_La.setObjectName("Circle_CentralY_La")
        self.Circle_CentralX_La = QtWidgets.QLabel(self.Mode_Circle_GB)
        self.Circle_CentralX_La.setGeometry(QtCore.QRect(100, 30, 61, 16))
        self.Circle_CentralX_La.setLineWidth(2)
        self.Circle_CentralX_La.setObjectName("Circle_CentralX_La")
        self.Circle_R_Box = QtWidgets.QSpinBox(self.Mode_Circle_GB)
        self.Circle_R_Box.setGeometry(QtCore.QRect(10, 50, 81, 24))
        self.Circle_R_Box.setMaximum(120)
        self.Circle_R_Box.setObjectName("Circle_R_Box")
        self.Circle_CentralX_Box = QtWidgets.QSpinBox(self.Mode_Circle_GB)
        self.Circle_CentralX_Box.setGeometry(QtCore.QRect(100, 50, 81, 24))
        self.Circle_CentralX_Box.setMaximum(320)
        self.Circle_CentralX_Box.setObjectName("Circle_CentralX_Box")
        self.Circle_CentralY_Box = QtWidgets.QSpinBox(self.Mode_Circle_GB)
        self.Circle_CentralY_Box.setGeometry(QtCore.QRect(190, 50, 81, 24))
        self.Circle_CentralY_Box.setMaximum(320)
        self.Circle_CentralY_Box.setObjectName("Circle_CentralY_Box")
#Init value
        self.Circle_CentralX_Box.setValue(160)
        self.Circle_CentralY_Box.setValue(160)
        self.Circle_R_Box.setValue(80)
###################
#Disable circle boxes by default
        self.Circle_R_Box.lineEdit().setEnabled(False)
        self.Circle_CentralX_Box.lineEdit().setEnabled(False)
        self.Circle_CentralY_Box.lineEdit().setEnabled(False)
################################
        self.Mode_Rectangle_RB = QtWidgets.QGroupBox(self.Mode_Fr)
        self.Mode_Rectangle_RB.setGeometry(QtCore.QRect(10, 130, 291, 141))
        self.Mode_Rectangle_RB.setObjectName("Mode_Rectangle_RB")
        self.Rectangle_TopLeftX_La = QtWidgets.QLabel(self.Mode_Rectangle_RB)
        self.Rectangle_TopLeftX_La.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.Rectangle_TopLeftX_La.setLineWidth(2)
        self.Rectangle_TopLeftX_La.setObjectName("Rectangle_TopLeftX_La")
        self.Rectangle_BotRightX_La = QtWidgets.QLabel(self.Mode_Rectangle_RB)
        self.Rectangle_BotRightX_La.setGeometry(QtCore.QRect(170, 30, 101, 16))
        self.Rectangle_BotRightX_La.setLineWidth(2)
        self.Rectangle_BotRightX_La.setObjectName("Rectangle_BotRightX_La")
        self.Rectangle_TopLeftY_La = QtWidgets.QLabel(self.Mode_Rectangle_RB)
        self.Rectangle_TopLeftY_La.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.Rectangle_TopLeftY_La.setLineWidth(2)
        self.Rectangle_TopLeftY_La.setObjectName("Rectangle_TopLeftY_La")
        self.Rectangle_BotRightY_La = QtWidgets.QLabel(self.Mode_Rectangle_RB)
        self.Rectangle_BotRightY_La.setGeometry(QtCore.QRect(170, 80, 101, 16))
        self.Rectangle_BotRightY_La.setLineWidth(2)
        self.Rectangle_BotRightY_La.setObjectName("Rectangle_BotRightY_La")
        self.Rectangle_TopLeftX_Box = QtWidgets.QSpinBox(self.Mode_Rectangle_RB)
        self.Rectangle_TopLeftX_Box.setGeometry(QtCore.QRect(40, 50, 81, 24))
        self.Rectangle_TopLeftX_Box.setMaximum(320)
        self.Rectangle_TopLeftX_Box.setObjectName("Rectangle_TopLeftX_Box")
        self.Rectangle_TopLeftY_Box = QtWidgets.QSpinBox(self.Mode_Rectangle_RB)
        self.Rectangle_TopLeftY_Box.setGeometry(QtCore.QRect(40, 100, 81, 24))
        self.Rectangle_TopLeftY_Box.setMaximum(320)
        self.Rectangle_TopLeftY_Box.setObjectName("Rectangle_TopLeftY_Box")
        self.Rectangle_BotRightX_Box = QtWidgets.QSpinBox(self.Mode_Rectangle_RB)
        self.Rectangle_BotRightX_Box.setGeometry(QtCore.QRect(170, 50, 81, 24))
        self.Rectangle_BotRightX_Box.setMaximum(320)
        self.Rectangle_BotRightX_Box.setObjectName("Rectangle_BotRightX_Box")
        self.Rectangle_BotRightY_Box = QtWidgets.QSpinBox(self.Mode_Rectangle_RB)
        self.Rectangle_BotRightY_Box.setGeometry(QtCore.QRect(170, 100, 81, 24))
        self.Rectangle_BotRightY_Box.setMaximum(320)
        self.Rectangle_BotRightY_Box.setObjectName("Rectangle_BotRightY_Box")
#Init value
        self.Rectangle_TopLeftX_Box.setValue(100)
        self.Rectangle_TopLeftY_Box.setValue(100)
        self.Rectangle_BotRightX_Box.setValue(220)
        self.Rectangle_BotRightY_Box.setValue(220)
###################
#Disable Rectangle box by default
        self.Rectangle_TopLeftX_Box.lineEdit().setEnabled(False)
        self.Rectangle_TopLeftY_Box.lineEdit().setEnabled(False)
        self.Rectangle_BotRightX_Box.lineEdit().setEnabled(False)
        self.Rectangle_BotRightY_Box.lineEdit().setEnabled(False)
#################################
        self.Mode_FreeSet_GB = QtWidgets.QGroupBox(self.Mode_Fr)
        self.Mode_FreeSet_GB.setGeometry(QtCore.QRect(10, 270, 291, 71))
        self.Mode_FreeSet_GB.setObjectName("Mode_FreeSet_GB")
        self.FreeSet_X_La = QtWidgets.QLabel(self.Mode_FreeSet_GB)
        self.FreeSet_X_La.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.FreeSet_X_La.setLineWidth(2)
        self.FreeSet_X_La.setObjectName("FreeSet_X_La")
        self.FreeSet_Y_La = QtWidgets.QLabel(self.Mode_FreeSet_GB)
        self.FreeSet_Y_La.setGeometry(QtCore.QRect(150, 30, 16, 16))
        self.FreeSet_Y_La.setLineWidth(2)
        self.FreeSet_Y_La.setObjectName("FreeSet_Y_La")
        self.FreeSet_X_Box = QtWidgets.QSpinBox(self.Mode_FreeSet_GB)
        self.FreeSet_X_Box.setGeometry(QtCore.QRect(40, 30, 81, 24))
        self.FreeSet_X_Box.setMaximum(320)
        self.FreeSet_X_Box.setObjectName("FreeSet_X_Box")
        self.FreeSet_Y_Box = QtWidgets.QSpinBox(self.Mode_FreeSet_GB)
        self.FreeSet_Y_Box.setGeometry(QtCore.QRect(170, 30, 81, 24))
        self.FreeSet_Y_Box.setMaximum(320)
        self.FreeSet_Y_Box.setObjectName("FreeSet_Y_Box")
#Init value
        self.FreeSet_X_Box.setValue(160)
        self.FreeSet_Y_Box.setValue(160)
###################
        self.Mode_Apply_Bu = QtWidgets.QPushButton(self.Mode_Fr)
        self.Mode_Apply_Bu.setGeometry(QtCore.QRect(12, 340, 291, 32))
        self.Mode_Apply_Bu.setObjectName("Mode_Apply_Bu")
#Add button callback
        self.Mode_Apply_Bu.clicked.connect(self.BAP_Mode_Apply)
####################
        self.Mode_Circle_Ch = QtWidgets.QRadioButton(self.Mode_Fr)
        self.Mode_Circle_Ch.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.Mode_Circle_Ch.setObjectName("Mode_Circle_Ch")
#Unchecked by default
        self.Mode_Circle_Ch.toggled.connect(self.BAP_Mode_Circle_Toggle)
        self.Mode_Circle_Ch.setChecked(False)
###################
        self.Mode_Rectangle_Ch = QtWidgets.QRadioButton(self.Mode_Fr)
        self.Mode_Rectangle_Ch.setGeometry(QtCore.QRect(100, 20, 91, 20))
        self.Mode_Rectangle_Ch.setObjectName("Mode_Rectangle_Ch")
#Unchecked by default
        self.Mode_Rectangle_Ch.toggled.connect(self.BAP_Mode_Rectangle_Toggle)
        self.Mode_Rectangle_Ch.setChecked(False)
###################
        self.Mode_FreeSet_Ch = QtWidgets.QRadioButton(self.Mode_Fr)
        self.Mode_FreeSet_Ch.setGeometry(QtCore.QRect(210, 20, 81, 20))
        self.Mode_FreeSet_Ch.setObjectName("Mode_FreeSet_Ch")
#Checked by default
        self.Mode_FreeSet_Ch.toggled.connect(self.BAP_Mode_FreeSet_Toggle)
        self.Mode_FreeSet_Ch.setChecked(True)
###################
        self.PlateView_Gra = pg.PlotWidget(self.centralWidget)
        self.PlateView_Gra.setGeometry(QtCore.QRect(330, 20, 400, 400))
        self.PlateView_Gra.setInteractive(False)
        self.PlateView_Gra.setObjectName("PlateView_Gra")
        self.PlateView_Gra.setXRange(0, 320, padding = 0)
        self.PlateView_Gra.setYRange(0, 320, padding = 0)
        self.PlateView_Gra.getViewBox().invertY(True)

        self.XAxist_Angle_Gra = pg.PlotWidget(self.centralWidget)
        self.XAxist_Angle_Gra.setGeometry(QtCore.QRect(330, 440, 400, 120))
        self.XAxist_Angle_Gra.setInteractive(False)
        self.XAxist_Angle_Gra.setObjectName("XAxist_Angle_Gra")
        self.XAxist_Angle_Gra.setXRange(0, 20, padding = 0)
        self.XAxist_Angle_Gra.setYRange(-12, 12, padding = 0)

        self.YAxist_Angle_Gra = pg.PlotWidget(self.centralWidget)
        self.YAxist_Angle_Gra.setGeometry(QtCore.QRect(330, 580, 400, 120))
        self.YAxist_Angle_Gra.setInteractive(False)
        self.YAxist_Angle_Gra.setObjectName("YAxist_Angle_Gra")
        self.YAxist_Angle_Gra.setXRange(0, 20, padding = 0)
        self.YAxist_Angle_Gra.setYRange(-12, 12, padding = 0)

        self.PlateView_Controller_La = QtWidgets.QLabel(self.centralWidget)
        self.PlateView_Controller_La.setGeometry(QtCore.QRect(700, 20, 30, 16))
        self.PlateView_Controller_La.setObjectName("PlateView_Controller_La")
        self.PlateView_Controller_La.setStyleSheet('color: white')

        self.PlateView_Mode_La = QtWidgets.QLabel(self.centralWidget)
        self.PlateView_Mode_La.setGeometry(QtCore.QRect(700, 40, 30, 16))
        self.PlateView_Mode_La.setObjectName("PlateView_Mode_La")
        self.PlateView_Mode_La.setStyleSheet('color: white')

        self.PlateView_La = QtWidgets.QLabel(self.centralWidget)
        self.PlateView_La.setGeometry(QtCore.QRect(330, 0, 91, 16))
        self.PlateView_La.setObjectName("PlateView_La")

        self.XAxist_Angle_La = QtWidgets.QLabel(self.centralWidget)
        self.XAxist_Angle_La.setGeometry(QtCore.QRect(330, 420, 91, 16))
        self.XAxist_Angle_La.setObjectName("XAxist_Angle_La")

        self.YAxist_Angle_La = QtWidgets.QLabel(self.centralWidget)
        self.YAxist_Angle_La.setGeometry(QtCore.QRect(330, 560, 91, 16))
        self.YAxist_Angle_La.setObjectName("YAxist_Angle_La")

        self.Parsing = ParsingThread(self.recvmsg)
        # self.Parsing.graph_update.connect(self.BAP_GraphUpdate)
        self.Parsing.start()

        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ball And Plate Control Panel"))
        self.Plate_Controller_La.setText(_translate("MainWindow", "Plate Controller"))
        self.PlateView_Controller_La.setText(_translate("MainWindow", "PID"))
        self.PlateView_Mode_La.setText(_translate("MainWindow", "FSe"))
        self.Plate_Controller_Apply_Bu.setText(_translate("MainWindow", "Apply"))
        self.Plate_Controller_PID_GB.setTitle(_translate("MainWindow", "PID Controller"))
        self.PID_Kp_La.setText(_translate("MainWindow", "Kp"))
        self.PID_Kd_La.setText(_translate("MainWindow", "Kd"))
        self.PID_Ki_La.setText(_translate("MainWindow", "Ki"))
        self.Plate_Controller_SMC_GB.setTitle(_translate("MainWindow", "Sliding Mode Control"))
        self.SMC_k1_La.setText(_translate("MainWindow", "k1"))
        self.SMC_K_La.setText(_translate("MainWindow", "K"))
        self.Plate_Controller_PID_Ch.setText(_translate("MainWindow", "PID"))
        self.Plate_Controller_SMC_Ch.setText(_translate("MainWindow", "SMC"))
        self.Mode_La.setText(_translate("MainWindow", "Mode"))
        self.Mode_Circle_GB.setTitle(_translate("MainWindow", "Circle Mode"))
        self.Circle_R_La.setText(_translate("MainWindow", "R"))
        self.Circle_CentralY_La.setText(_translate("MainWindow", "Central Y"))
        self.Circle_CentralX_La.setText(_translate("MainWindow", "Central X"))
        self.Mode_Rectangle_RB.setTitle(_translate("MainWindow", "Rectangle Mode"))
        self.Rectangle_TopLeftX_La.setText(_translate("MainWindow", "Top Left X"))
        self.Rectangle_BotRightX_La.setText(_translate("MainWindow", "Bottom Right X"))
        self.Rectangle_TopLeftY_La.setText(_translate("MainWindow", "Top Left Y"))
        self.Rectangle_BotRightY_La.setText(_translate("MainWindow", "Bottom Right Y"))
        self.Mode_FreeSet_GB.setTitle(_translate("MainWindow", "Free Set Mode"))
        self.FreeSet_X_La.setText(_translate("MainWindow", "X"))
        self.FreeSet_Y_La.setText(_translate("MainWindow", "Y"))
        self.Mode_Apply_Bu.setText(_translate("MainWindow", "Apply"))
        self.Mode_Circle_Ch.setText(_translate("MainWindow", "Circle"))
        self.Mode_Rectangle_Ch.setText(_translate("MainWindow", "Rectangle"))
        self.Mode_FreeSet_Ch.setText(_translate("MainWindow", "Free Set"))
        self.PlateView_La.setText(_translate("MainWindow", "Plate View"))
        self.XAxist_Angle_La.setText(_translate("MainWindow", "X Axist Angle"))
        self.YAxist_Angle_La.setText(_translate("MainWindow", "Y Axist Angle"))

    def BAP_Controller_Apply(self):
        if(self.Plate_Controller_PID_Ch.isChecked()):
            Kp = self.PID_Kp_Box.value()
            Ki = self.PID_Ki_Box.value()
            Kd = self.PID_Kd_Box.value()
            UARTStr = '[Ctrl][PID][' + '%1.4f '%Kp + '%1.4f '%Ki + '%1.4f]'%Kd
            length = len(UARTStr) + 4
            lenStr = '[' + '%02d'%length + ']'
            SendStr = lenStr + UARTStr
            BAP_SendMsgQueueMutex.acquire()
            BAP_SendMsgQueue.put(SendStr.ljust(40, ' '))
            BAP_SendMsgQueueMutex.release()
            BAP_SendMsgQueueSem.release()

        elif(self.Plate_Controller_SMC_Ch.isChecked()):
            k1 = self.SMC_k1_Box.value()
            K = self.SMC_K_Box.value()
            UARTStr = '[Ctrl][SMC][' + '%1.4f '%K + '%1.4f]'%k1
            length = len(UARTStr) + 4
            lenStr = '[' + '%02d'%length + ']'
            SendStr = lenStr + UARTStr
            BAP_SendMsgQueueMutex.acquire()
            BAP_SendMsgQueue.put(SendStr.ljust(40, ' '))
            BAP_SendMsgQueueMutex.release()
            BAP_SendMsgQueueSem.release()

    def BAP_Mode_Apply(self):
        print "BAP_Mode_Apply"
        if(self.Mode_Circle_Ch.isChecked()):
            R = self.Circle_R_Box.value()
            x = self.Circle_CentralX_Box.value()
            y = self.Circle_CentralY_Box.value()
            UARTStr = '[Mode][Cir][' + '%03d '%R + '%03d '%x + '%03d]'%y
            length = len(UARTStr) + 4
            lenStr = '[' + '%02d'%length + ']'
            SendStr = lenStr + UARTStr
            BAP_SendMsgQueueMutex.acquire()
            BAP_SendMsgQueue.put(SendStr.ljust(40, ' '))
            BAP_SendMsgQueueMutex.release()
            BAP_SendMsgQueueSem.release()

        elif(self.Mode_Rectangle_Ch.isChecked()):
            tlx = self.Rectangle_TopLeftX_Box.value()
            tly = self.Rectangle_TopLeftY_Box.value()
            brx = self.Rectangle_BotRightX_Box.value()
            bry = self.Rectangle_BotRightY_Box.value()
            UARTStr = '[Mode][Rec][' + '%03d '%tlx + '%03d '%tly + '%03d '%brx + '%03d]'%bry
            length = len(UARTStr) + 4
            lenStr = '[' + '%02d'%length + ']'
            SendStr = lenStr + UARTStr
            BAP_SendMsgQueueMutex.acquire()
            BAP_SendMsgQueue.put(SendStr.ljust(40, ' '))
            BAP_SendMsgQueueMutex.release()
            BAP_SendMsgQueueSem.release()

        elif(self.Mode_FreeSet_Ch.isChecked()):
            fx = self.FreeSet_X_Box.value()
            fy = self.FreeSet_Y_Box.value()
            UARTStr = '[Mode][FSe][' + '%03d '%fx + '%03d]'%fy
            length = len(UARTStr) + 4
            lenStr = '[' + '%02d'%length + ']'
            SendStr = lenStr + UARTStr
            BAP_SendMsgQueueMutex.acquire()
            BAP_SendMsgQueue.put(SendStr.ljust(40, ' '))
            BAP_SendMsgQueueMutex.release()
            BAP_SendMsgQueueSem.release()

    def BAP_Controller_PID_Toggle(self):
        if(self.Plate_Controller_PID_Ch.isChecked()):
            self.PID_Kp_Box.lineEdit().setEnabled(True)
            self.PID_Ki_Box.lineEdit().setEnabled(True)
            self.PID_Kd_Box.lineEdit().setEnabled(True)
        else:
            self.PID_Kp_Box.lineEdit().setEnabled(False)
            self.PID_Ki_Box.lineEdit().setEnabled(False)
            self.PID_Kd_Box.lineEdit().setEnabled(False)

    def BAP_Controller_SMC_Toggle(self):
        if(self.Plate_Controller_SMC_Ch.isChecked()):
            self.SMC_K_Box.lineEdit().setEnabled(True)
            self.SMC_k1_Box.lineEdit().setEnabled(True)
        else:
            self.SMC_K_Box.lineEdit().setEnabled(False)
            self.SMC_k1_Box.lineEdit().setEnabled(False)            

    def BAP_Mode_Circle_Toggle(self):
        if(self.Mode_Circle_Ch.isChecked()):
            self.Circle_R_Box.lineEdit().setEnabled(True)
            self.Circle_CentralX_Box.lineEdit().setEnabled(True)
            self.Circle_CentralY_Box.lineEdit().setEnabled(True)
        else:
            self.Circle_R_Box.lineEdit().setEnabled(False)
            self.Circle_CentralX_Box.lineEdit().setEnabled(False)
            self.Circle_CentralY_Box.lineEdit().setEnabled(False)

    def BAP_Mode_Rectangle_Toggle(self):
        if(self.Mode_Rectangle_Ch.isChecked()):
            self.Rectangle_TopLeftX_Box.lineEdit().setEnabled(True)
            self.Rectangle_TopLeftY_Box.lineEdit().setEnabled(True)
            self.Rectangle_BotRightX_Box.lineEdit().setEnabled(True)
            self.Rectangle_BotRightY_Box.lineEdit().setEnabled(True)
        else:
            self.Rectangle_TopLeftX_Box.lineEdit().setEnabled(False)
            self.Rectangle_TopLeftY_Box.lineEdit().setEnabled(False)
            self.Rectangle_BotRightX_Box.lineEdit().setEnabled(False)
            self.Rectangle_BotRightY_Box.lineEdit().setEnabled(False)

    def BAP_Mode_FreeSet_Toggle(self):
        if(self.Mode_FreeSet_Ch.isChecked()):
            self.FreeSet_X_Box.lineEdit().setEnabled(True)
            self.FreeSet_Y_Box.lineEdit().setEnabled(True)
        else:
            self.FreeSet_X_Box.lineEdit().setEnabled(False)
            self.FreeSet_Y_Box.lineEdit().setEnabled(False)

    def BAP_GraphUpdate(self):
        global BAP_SharedVarsList
        time_count = 0
        while (self.Running == 1):
            time_count += 0.02
            BAP_SharedVarsMutex.acquire()
            Lst = BAP_SharedVarsList[:]
            BAP_SharedVarsMutex.release()
            self.PlateView_Controller_La.setText(Lst[8])
            self.PlateView_Mode_La.setText(Lst[9])
            self.XAxist_Angle_Gra.plot([time_count], [0])
            # self.YAxist_Angle_Gra.plot([time_count], Lst[5])
            if(time_count >= 20):
                time_count = 0
            sleep(0.01)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Parsing thread
class ParsingThread(QtCore.QThread):
    graph_update = QtCore.pyqtSignal(int)

    def __init__(self, RecvMsgQueue):
        QtCore.QThread.__init__(self)
        self.RecvMsgQueue = RecvMsgQueue
        self.Running = 1

    def run(self):
        global BAP_SharedVarsList
        while (self.Running == 1):
            if not self.RecvMsgQueue.empty():
                data = self.RecvMsgQueue.get()
                parse = data.split()
                if (len(parse) == 12 and parse[0] == "[Strm]["):
                    BAP_SharedVarsMutex.acquire()
                    BAP_SharedVarsList[0] = int(parse[1])
                    BAP_SharedVarsList[1] = int(parse[2])
                    BAP_SharedVarsList[2] = int(parse[3])
                    BAP_SharedVarsList[3] = int(parse[4])
                    BAP_SharedVarsList[4] = float(parse[5])
                    BAP_SharedVarsList[5] = float(parse[6])
                    BAP_SharedVarsList[6] = float(parse[7])
                    BAP_SharedVarsList[7] = float(parse[8])
                    BAP_SharedVarsList[8] = parse[9]
                    BAP_SharedVarsList[9] = parse[10]
                    BAP_SharedVarsMutex.release()
                    self.graph_update.emit(1)

    def destroy(self):
        self.Running = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    BAP_UI = Ui_MainWindow(MainWindow, BAP_RecvMsgQueue)

    BAP_RecvThread = UARTCommand.RecvThread(BAP_RecvMsgQueue)
    BAP_SendThread = UARTCommand.SendThread(BAP_SendMsgQueue, BAP_SendMsgQueueMutex, BAP_SendMsgQueueSem)

    BAP_RecvThread.start()
    BAP_SendThread.start()

    MainWindow.show()
    sys.exit(app.exec_())

