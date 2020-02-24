import zmq
import os
import time
import sys

def collector3(port):
    """
    Receives images from consumer 2
    :param port: port to receive from
    :return: nothing
    """
    context = zmq.Context()
    collector1_rec = context.socket(zmq.PULL)
    collector1_rec.bind("tcp://127.0.0.1:%s" % port)

    if not os.path.exists('results'):
        os.makedirs('results')

    while True:
        msg = collector1_rec.recv_pyobj()
        print('msg received from consumer2')
        f = open('results/' + msg['name']+".txt", "w+")
        for cont_name in msg['conts']:
            string = "This contor of " + (cont_name) +" x0 " + str(msg['conts'][cont_name]['x0']) + " y0 " + \
                     str(msg['conts'][cont_name]['y0']) + " x2 " + str(msg['conts'][cont_name]['x2']) +" y2 " + \
                     str(msg['conts'][cont_name]['y2']) + '\n\n'
            f.write(string)
        time.sleep(1)


port = int(sys.argv[1])
collector3(port)
