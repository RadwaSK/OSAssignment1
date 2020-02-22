import zmq
from utils import *
import sys

def server(port, video_name):
    """
    Re-samples given video to images, sends them to port
    :param port: port to send on
    :param video_name: Name of video (with extension)
    :return: nothing
    """
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://127.0.0.1:%s" % port)

    if not os.path.exists('images'):
        os.makedirs('images')
        resample_video_frames(30, 1, video_name, 'images')

    images, names = read_images(r'images')

    for img, name in zip(images, names):
        msg = {'data': img, 'name': name}
        socket.send_pyobj(msg)
        # msg = socket.recv()
        print('send image to consumer1')

port = int(sys.argv[1])
video = sys.argv[2]
server(port, video)
