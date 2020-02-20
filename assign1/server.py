import zmq
import random
import sys
import time
import numpy as np
from utils import *


port = "5555"

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:%s" % port)

if os.path.exists('images') == False:
    os.makedirs('images')
    resample_video_frames(30, 5, 'checkerboard.mp4', 'images')

images, names = read_images(r'images')

for img, name in zip(images, names):
    msg = {'data': img, 'name': name}
    # socket.send_pyobj(msg)
    # msg = socket.recv()
    # print(msg)