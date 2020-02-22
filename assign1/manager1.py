from server.py import *
from collector1.py import *
from consumer1.py import *
import sys
import time


N = sys.argv[1]
video = sys.argv[2]

collectors = []
consumers = []

server_port = 5555
starting_port_for_consumers = 5556
starting_port_for_collectors = starting_port_for_consumers + N

N_collectors =  int((N-1) / 2) + 1

for i in range(N_collectors):
	collectors.append(collector1(starting_port_for_consumers, starting_port_for_collectors))
	# collectors.append((starting_port_for_consumers, starting_port_for_collectors))
	starting_port_for_collectors += 1
	if i % 2 == 1:
		starting_port_for_consumers += 1

starting_port_for_consumers = 5556

for i in range(N):
	consumers.append(consumer1(server_port, starting_port_for_consumers))
	# consumers.append((server_port, starting_port_for_consumers))
	if i % 2 == 1:
		starting_port_for_consumers += 1


# for con in consumers:
# 	print(con)

# print()

# for col in collectors:
# 	print(col)