import zmq 
import random
import sys
import time

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:%s" % port) # fe wa7ed 3amel port w 3ayez a3ml m3ah connect

while True:
    msg = socket.recv()
    print(msg)
    socket.send_string("cliecnt message to server1")
    socket.send_string("cliecnt message to server2")
    time.sleep(1)