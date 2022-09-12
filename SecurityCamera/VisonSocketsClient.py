import socket
import sys
import cv2
import pickle
import numpy as np
import struct

HOST = 'XXX.XXX.XXX.XXX'
PORT = XXXXX

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Listening to Socket')
conn, addr = s.accept()

data = b''

while True:
    while data.find(b'STOP!') < 0:
        data += conn.recv(90456)

    frameData = data[:data.find(b'STOP!')]
    data = data[data.find(b'STOP!'):].replace(b'STOP!', b'')

    frame = pickle.loads(frameData)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        s
        break

