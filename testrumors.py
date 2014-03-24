from rumor import *

tests = 1000
size = 10
turns = 8

algos = [Push_alg, Pull_alg, PushPull_alg, Median_Ctr_alg]

#Do each algo without sharing
for algo in algos:
	connections = [0.0] * turns
	transmissions = [0.0] * turns
	informed = [0.0] * turns

	for _ in range(0,tests):
		b = algo(size)
		#print b.algorithm
		for turn in range(0,turns):
			b.do_turn(1)
			connections[turn] += (b.connections_made + 0.0) / tests
			transmissions[turn] += (b.transmissions_made + 0.0) / tests
			informed[turn] += (b.the_net.informed() + 0.0) / tests
			#print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)
			#if algo is Median_Ctr_alg:
			#print "ctrmax: %d" % b.the_net.Nodes[0].ctrMax

	
	print "%s: Average stats: (Connections %s) (Transmissions %s) (Informed %s / %d)" % (b.algorithm, connections, transmissions, informed, size)
	print
		
#do each algo with sharing
for algo in algos:
	connections = [0.0] * turns
	transmissions = [0.0] * turns
	informed = [0.0] * turns

	for _ in range(0,tests):
		b = algo(size, True)
		#print b.algorithm
		for turn in range(0,turns):
			b.do_turn(1)
			connections[turn] += (b.connections_made + 0.0) / tests
			transmissions[turn] += (b.transmissions_made + 0.0) / tests
			informed[turn] += (b.the_net.informed() + 0.0) / tests
			#print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)
			#if algo is Median_Ctr_alg:
			#print "ctrmax: %d" % b.the_net.Nodes[0].ctrMax

	
	print "%s: Average stats: (Connections %s) (Transmissions %s) (Informed %s / %d)" % (b.algorithm, connections, transmissions, informed, size)
	print
"""
print "Pushing"
b = Push_alg(size)
b.do_turn(turns)
print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)

print "Pulling"
b = Pull_alg(size)
b.do_turn(turns)
print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)

print "PushPulling"
b = PushPull_alg(size)
b.do_turn(turns)
print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)

print "Median Counting"
b = Median_Ctr_alg(size)
b.do_turn(turns)
print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)
print "ctrmax: %d" % b.the_net.Nodes[0].ctrMax
"""
