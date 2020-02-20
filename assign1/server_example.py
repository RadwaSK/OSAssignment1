import zmq 
import random
import sys
import time

port = "5556"

context = zmq.Context()
#zmq by3ml 2 queues recv and send
socket = context.socket(zmq.PAIR) # pair -> wa7ed osad wa7ed 
socket.bind("tcp://127.0.0.1:%s" % port)

while True:
    #3ndna 2 queues one for recv and another for send
    socket.send_string("Server message to client3")
    msg = socket.recv()
    print(msg)