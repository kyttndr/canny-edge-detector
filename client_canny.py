import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import io
import json
import pickle

cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8088))

while(cap.isOpened()):
  ret, frame = cap.read()

  frame = cv2.resize(frame, (480, 320))

  # Canny
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # print(frame.shape)
  frame = cv2.Canny(frame, 100, 200)


  data = pickle.dumps(frame)

  clientsocket.sendall(struct.pack("L", len(data)) + data)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
