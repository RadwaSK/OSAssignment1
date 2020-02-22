from collector3 import *
from consumer2 import *
import sys
import time



N = int(sys.argv[1])

consumers = []

collector3_port = 5540
starting_port_for_consumer2 = 5556+N

collector3(collector3_port)

for i in range(N):
    consumer2(starting_port_for_consumer2, collector3_port)
    # print(starting_port_for_consumer2, collector3_port)
    if i % 2 == 1:
        starting_port_for_consumer2 += 1


