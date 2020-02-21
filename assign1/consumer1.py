import zmq
import cv2


def consumer1(port1, port2):
    """
    Receives images from port1, threshold it and send it to port2
    :param port1: port to receive from
    :param port2: port to send to
    :return: nothing
    """
    context = zmq.Context()
    consumer1_rec = context.socket(zmq.PULL)
    consumer1_rec.connect("tcp://127.0.0.1:%s" % port1)

    consumer1_sender = context.socket(zmq.PUSH)
    consumer1_sender.connect("tcp://127.0.0.1:%s" % port2)

    while True:
        msg = consumer1_rec.recv_pyobj()
        # print(msg)
        img = msg['data']
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        msg['data'] = img
        consumer1_sender.send_pyobj(msg)
        # time.sleep(1)

