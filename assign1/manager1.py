import sys
import os


N = int(sys.argv[1])
video = sys.argv[2]

# collectors = []
# consumers = []

server_port = 5555
starting_port_for_consumers = 5556
starting_port_for_collectors = starting_port_for_consumers + N

N_collectors = int((N-1) / 2) + 1

cmd = 'python server.py ' + str(server_port) + ' ' + video + ' & '

for i in range(N_collectors):
	cmd += 'python collector1.py ' + str(starting_port_for_consumers) + ' ' + str(starting_port_for_collectors) + ' & '
	starting_port_for_collectors += 1
	starting_port_for_consumers += 1

starting_port_for_consumers = 5556

for i in range(N):
	if i != N - 1:
		cmd += 'python consumer1.py ' + str(server_port) + ' ' + str(starting_port_for_consumers) + ' & '
	else:
		cmd += 'python consumer1.py ' + str(server_port) + ' ' + str(starting_port_for_consumers)
	if i % 2 == 1:
		starting_port_for_consumers += 1

# print(cmd)
os.system(cmd)
