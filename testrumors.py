from rumor import *

tests = 3
size = 1000
turns = 8

algos = [Push_alg, Pull_alg, PushPull_alg, Median_Ctr_alg]

#Do each algo without sharing
for algo in algos:
	b = algo(size)
	print b.algorithm
	b.do_turn(turns)
	print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)
	if algo is Median_Ctr_alg:
		print "ctrmax: %d" % b.the_net.Nodes[0].ctrMax
		
#do each algo with sharing
for algo in algos:
	b = algo(size, True)
	print b.algorithm + " Sharing"
	b.do_turn(turns)
	print "connections: %d transmissions: %d Informed: %d / %d" % (b.connections_made, b.transmissions_made, b.the_net.informed(), b.the_net.size)
	if algo is Median_Ctr_alg:
		print "ctrmax: %d" % b.the_net.Nodes[0].ctrMax
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
