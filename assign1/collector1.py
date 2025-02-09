import zmq
import cv2
import time
import sys

def collector1(port1, port2):
    """
    Receives images from port1, and send it to port2
    :param port1: port to receive from
    :param port2: port to send to
    :return: nothing
    """
    context = zmq.Context()
    collector1_rec = context.socket(zmq.PULL)
    collector1_rec.bind("tcp://127.0.0.1:%s" % port1)

    collector1_sender = context.socket(zmq.PUSH)
    collector1_sender.bind("tcp://*:%s" % port2)

    while True:
        msg = collector1_rec.recv_pyobj()
        print('msg received from consumer1')
        collector1_sender.send_pyobj(msg)
        print('msg sent to consumer2')
        time.sleep(1)

port1 = int(sys.argv[1])
port2 = int(sys.argv[2])
collector1(port1, port2)
