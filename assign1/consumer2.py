import zmq
import cv2
import time
import sys


def consumer2(port1, port2):
    """
    Receives images from port1, finds contours
    and send json object with data of contours to port2
    :param port1: port to receive from
    :param port2: port to send to
    :return: nothing
    """
    context = zmq.Context()
    consumer1_rec = context.socket(zmq.PULL)
    consumer1_rec.connect("tcp://127.0.0.1:%s" % port1)

    consumer1_sender = context.socket(zmq.PUSH)
    consumer1_sender.bind("tcp://127.0.0.1:%s" % port2)


    while True:
        msg = consumer1_rec.recv_pyobj()
        print('msg received from collector1')
        img = msg['data']
        name = msg['name']
        binary_img, contours, heirachy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        msg = {'name': name}
        all_conts = {}
        for j, cont in enumerate(contours):
            cont_name = 'cont' + str(j)
            bounding_box = cv2.boxPoints(cv2.minAreaRect(cont))
            coords = {}
            for i, p in enumerate(bounding_box):
                x = 'x' + str(i)
                y = 'y' + str(i)
                coords[x] = p[0]
                coords[y] = p[1]
            all_conts[cont_name] = coords
        msg['conts'] = all_conts
        consumer1_sender.send_pyobj(msg)
        print('msg sent to collector3')
        time.sleep(1)


port1 = int(sys.argv[1])
port2 = int(sys.argv[2])
consumer2(port1, port2)
