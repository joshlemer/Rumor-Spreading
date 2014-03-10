import random

class Node:
	def __init__(self, net, index):
		self.index = index
		self.knows_rumor = False
		self.ctr = 0
		self.state = 'A'
		self.net = net
	
	def tell_rumor(self):
		self.knows_rumor = True
		
		if self.state is 'A': self.state = 'B'

	
class Network:
	def __init__(self, size):
		self.size = size
		self.Nodes = []
		for _ in range(0, size):
			self.Nodes.append(Node(self, _))
	
	def rand_src(self):
		rand = random.choice(self.Nodes)
		rand.ctr = 1
		rand.state = 'B'
		rand.knows_rumor = True
	
	def print_net(self):
		for Node in self.Nodes:
			num = 0
			if Node.knows_rumor: num = 1
			print ("(%d %d)" % (Node.index, Node.knows_rumor)),
		print "\n"

class  Push_alg:
	def __init__(self, size):
		self.the_net = Network(size)
		self.the_net.rand_src()
		self.turns_elapsed = 0

	def do_turn(self, turns):

		for _ in range(0, turns):
			nodes_to_tell = []

			for Node in self.the_net.Nodes:
				if Node.knows_rumor:
					rand = random.choice(Node.net.Nodes)
					nodes_to_tell.append(rand)

			for Node in nodes_to_tell:
				Node.tell_rumor()

			self.turns_elapsed += 1
			
b = Push_alg(10)
b.the_net.print_net()

for _ in range(0,10):
	b.do_turn(1)
	b.the_net.print_net()



					

		




