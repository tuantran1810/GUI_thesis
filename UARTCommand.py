#!/usr/bin/python
import Queue
import threading
import serial
import time

START_OF_TEXT_D = '\x02'
END_OF_TEXT_D = '\x03'
SERIAL_DEVICE = '/dev/tty.SLAB_USBtoUART'
SERIAL_SPEED = 230400

usleep = lambda x: time.sleep(x/1000000.0)

ser = serial.Serial(
    port = SERIAL_DEVICE,
    baudrate = SERIAL_SPEED,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 0.01
)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# UART receiving thread
class RecvThread (threading.Thread):

    def __init__(self, RecvMsgQueue):
        threading.Thread.__init__(self)
        self.RecvMsgQueue = RecvMsgQueue
        self.RecvRunning = 1

    def run(self):
        while (self.RecvRunning == 1):
            inData = ser.read(70)
            if(inData != ''):
                self.RecvMsgQueue.put(inData)

    def destroy(self):
        self.RecvRunning = 0

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Command processing thread
class SendThread (threading.Thread):

    def __init__(self, MsgQueue, Lock, Sem):
        threading.Thread.__init__(self)
        self.MsgQueue = MsgQueue
        self.Lock = Lock
        self.Sem = Sem
        self.SendRunning = 1

    def run(self):
        while (self.SendRunning == 1):
            self.Sem.acquire()
            self.Lock.acquire()
            if not self.MsgQueue.empty():
                data = self.MsgQueue.get()
                ser.write(data)
                print "Send: ", data
            self.Lock.release()

    def destroy(self):
        self.SendRunning = 0
