import sys
import time
import os


N = int(sys.argv[1])

consumers = []

collector3_port = 5540
starting_port_for_consumer2 = 5556+N

# collector3(collector3_port)

cmd = ''

for i in range(N):
    cmd += 'python consumer2.py ' + str(starting_port_for_consumer2) + ' ' + str(collector3_port) + ' & '
    # os.system(cmd)
    # consumer2(starting_port_for_consumer2, collector3_port)
    # print(starting_port_for_consumer2, collector3_port)
    if i % 2 == 1:
        starting_port_for_consumer2 += 1

cmd += 'python collector3.py ' + str(collector3_port)
# print(cmd)
os.system(cmd)
