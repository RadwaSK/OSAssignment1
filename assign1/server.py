import zmq
import pickle
import random
import sys
import time
import numpy as np
from utils import *

# First re-sample video if not already re-sampled
if os.path.exists('resampled_images') == False:
    os.makedirs('resampled_images')
    resample_video_frames(30, 3, 'checkerboard.mp4', 'resampled_images')

images, names = read_images(r'resampled_images')


# To know ports in use:
    # sudo lsof -i -P -n
port = "5555"

context = zmq.Context()
socket = context.socket(zmq.PUSH)
# print(socket.socket_type)

# local host
socket.bind("tcp://127.0.0.1:%s" % port)


for img, name in zip(images, names):
    msg = {'data': img, 'name': name}
    socket.send_pyobj(msg)
    # reply = socket.recv()
    # print(reply)