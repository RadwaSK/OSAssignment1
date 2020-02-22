import zmq
import cv2
import time

def collector3(port):
    """
    Receives images from consumer 2
    :param port: port to receive from
    :return: nothing
    """
    context = zmq.Context()
    collector1_rec = context.socket(zmq.PULL)
    collector1_rec.connect("tcp://127.0.0.1:%s" % port)

    while True:
        msg = collector1_rec.recv_pyobj()
       # msg = {'name': 'image', 'conts': {'cont0': {'x0': 499.0, 'y0': 499.0, 'x1': -1.5277469e-14, 'y1': 499.0, 'x2': 0.0, 'y2': 0.0, 'x3': 499.0, 'y3': 0.0}, 'cont1': {'x0': 199.0, 'y0': 400.0, 'x1': 199.0, 'y1': 299.0, 'x2': 300.0, 'y2': 299.0, 'x3': 300.0, 'y3': 400.0}, 'cont2': {'x0': 299.0, 'y0': 300.0, 'x1': 299.0, 'y1': 199.0, 'x2': 400.0, 'y2': 199.0, 'x3': 400.0, 'y3': 300.0}, 'cont3': {'x0': 99.0, 'y0': 300.0, 'x1': 99.0, 'y1': 199.0, 'x2': 200.0, 'y2': 199.0, 'x3': 200.0, 'y3': 300.0}, 'cont4': {'x0': 199.0, 'y0': 200.0, 'x1': 199.0, 'y1': 99.0, 'x2': 300.0, 'y2': 99.0, 'x3': 300.0, 'y3': 200.0}}}

        f = open(msg['name']+".txt", "w+")
        for cont_name in msg['conts']:
            string =  "This contor of " + (cont_name) +" x0 " + str(msg['conts'][cont_name]['x0']) + " y0 " + str(msg['conts'][cont_name]['y0']) + " x1 " + str(msg['conts'][cont_name]['x1']) +" y1 " + str(msg['conts'][cont_name]['y1'])
            f.write(string)
        time.sleep(1)

# collector3(5555)