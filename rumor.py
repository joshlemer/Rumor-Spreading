import random
import math
from sets import Set

class Node:
	def __init__(self, net, index):
		self.index = index
		self.knows_rumor = False
		self.ctr = 0
		self.state = 'A'
		self.net = net
		self.informed = Set([])
		self.c_ctr = 0
		self.BLessCtr = 0
		self.BGreaterOrEqCtr = 0
		self.ctrMax = math.log(math.log(self.net.size))
		self.cMax = self.ctrMax
		

	def tell_rumor(self, theMsg = None):

		self.knows_rumor = True
		self.informed = self.informed | Set([self.index])
		if theMsg is not None:
			self.informed = self.informed | theMsg.informed
			
			if self.state is 'A':
				if theMsg.stateFrom is 'B':
					self.state = 'B'
					self.ctr = 1
				else:
					#theMsg.stateFrom is 'C'
					self.state = 'C'
			elif self.state is 'B':
				if theMsg.ctrFrom < self.ctr: self.BLessCtr += 1
				else:
					self.BGreaterOrEqCtr += 1
				if theMsg.stateFrom is 'C':
					self.state = 'C'
		else:
			self.state = 'B'
			self.ctr = 1

class Msg:
#The Msg is thought to contain the rumor
	def __init__(self, from_Node, to_Node):

		self.fromNode = from_Node.index
		self.toNode = to_Node.index

		#state_of_from is the state of from_node at time of making Msg
		self.stateFrom = from_Node.state
		self.stateTo = to_Node.state

		#similar for ctr
		self.ctrFrom = from_Node.ctr
		self.ctrTo = to_Node.ctr

		self.informed = from_Node.informed
	
	def printMsg(self):
		print "From: %d To: %d" % (self.fromNode, self.toNode)

class Network:
	def __init__(self, size):
		self.size = size
		self.Nodes = []
		for _ in range(0, size):
			self.Nodes.append(Node(self, _))
	
	def rand_src(self):
		rand = random.choice(self.Nodes)
		rand.tell_rumor()
	
	def informed(self):
		count = 0
		for node in self.Nodes:
			if node.knows_rumor:
				count += 1
		return count

	def print_net(self):
		for Node in self.Nodes:
			num = 0
			if Node.knows_rumor: num = 1
			print ("(%d %s%d %d)" % (Node.index, Node.state, Node.ctr, Node.knows_rumor)),
		print "\n"
		
class Median_Ctr_alg:
	def __init__(self, size , sharing = False):
		self.the_net = Network(size)
		self.the_net.rand_src()
		self.turns_elapsed = 0
		self.connections_made = 0
		self.transmissions_made = 0
		self.sharing = sharing
		self.algorithm = "Median Counter Algorithm"
	
	def do_turn(self, turns):
		for _ in range(0, turns):
			messages = []

			for Node in self.the_net.Nodes:

				if Node.state is 'A':
					rand = random.choice(Node.net.Nodes)
					while rand.index == Node.index:
						rand = random.choice(Node.net.Nodes)

					self.connections_made += 1

					if rand.knows_rumor:
						messages.append(Msg(rand,Node))
						self.transmissions_made += 1
						

				elif Node.state is 'B' or Node.state is 'C':
					rand = random.choice(Node.net.Nodes)
					while rand.index == Node.index:
						rand = random.choice(Node.net.Nodes)

					if self.sharing and len(Node.informed) < self.the_net.size:
						rand = self.the_net.Nodes[random.sample(Set(range(0, self.the_net.size)) - Node.informed, 1)[0]]

					self.connections_made += 1
					messages.append(Msg(Node, rand))
					self.transmissions_made += 1

					if Node.state is 'C':
						Node.c_ctr += 1

			for message in messages:
				self.the_net.Nodes[message.toNode].tell_rumor(message)
				self.the_net.Nodes[message.fromNode].informed.add(message.toNode)

			#Now update all the B and C states (in case of Bm ->Bm+1, BctrMax+1 -> C or C->D
			for node in self.the_net.Nodes:
				if node.state is 'B' and node.BLessCtr < node.BGreaterOrEqCtr:	
					node.ctr += 1
					if node.ctr > node.ctrMax: node.state = 'C'

			 	elif node.c_ctr > node.cMax: node.state = 'D'


class Pull_alg:
	def __init__(self, size, sharing=False):
		self.the_net = Network(size)
		self.the_net.rand_src()
		self.turns_elapsed = 0
		self.connections_made = 0
		self.transmissions_made = 0
		self.sharing = sharing
		self.algorithm = "Pull Algorithm"
	
	def do_turn(self, turns):

		for _ in range(0, turns):
			messages = []
			
			for Node in self.the_net.Nodes:
				if not Node.knows_rumor:
					rand = random.choice(Node.net.Nodes)
					while rand.index == Node.index:
						rand = random.choice(Node.net.Nodes)

					self.connections_made += 1

					if rand.knows_rumor:
						messages.append(Msg(rand,Node))
						self.transmissions_made += 1

			for message in messages:
				self.the_net.Nodes[message.toNode].tell_rumor(message)
				self.the_net.Nodes[message.fromNode].informed.add(message.toNode)

			self.turns_elapsed += 1

class  Push_alg:
	def __init__(self, size, sharing=False):
		self.the_net = Network(size)
		self.the_net.rand_src()
		self.turns_elapsed = 0
		self.connections_made = 0
		self.transmissions_made = 0
		self.sharing = sharing
		self.algorithm = "Push Algorithm"
		self.messages = []

	def do_turn(self, turns):

		for _ in range(0, turns):
			messages = []

			for Node in self.the_net.Nodes:
				if Node.knows_rumor:
					rand = random.choice(Node.net.Nodes)
					while rand.index == Node.index:
						rand = random.choice(Node.net.Nodes)

					if self.sharing and len(Node.informed) < self.the_net.size:
						rand = self.the_net.Nodes[random.sample(Set(range(0, self.the_net.size)) - Node.informed, 1)[0]]

					self.connections_made += 1

					messages.append(Msg(Node,rand))
					self.transmissions_made += 1

			for message in messages:
				self.messages.append(message)
				self.the_net.Nodes[message.toNode].tell_rumor(message)
				self.the_net.Nodes[message.fromNode].informed.add(message.toNode)
				

			self.turns_elapsed += 1

class PushPull_alg:
	def __init__(self, size, sharing=False):
		self.the_net = Network(size)
		self.the_net.rand_src()
		self.turns_elapsed = 0
		self.connections_made = 0
		self.transmissions_made = 0
		self.sharing = sharing
		self.algorithm = "Push-Pull Algorithm"

	def do_turn(self, turns):
		
		for _ in range(0, turns):
			messages = []

			for Node in self.the_net.Nodes:
				rand = random.choice(Node.net.Nodes)
				while rand.index == Node.index:
					rand = random.choice(Node.net.Nodes)

				if Node.knows_rumor and self.sharing and len(Node.informed) < self.the_net.size:
					rand = self.the_net.Nodes[random.sample(Set(range(0, self.the_net.size)) - Node.informed, 1)[0]]

				self.connections_made += 1
				if Node.knows_rumor:
					messages.append(Msg(Node,rand))
					self.transmissions_made += 1

				elif rand.knows_rumor:
					messages.append(Msg(rand,Node))
					self.transmissions_made += 1

			for message in messages:
				self.the_net.Nodes[message.toNode].tell_rumor(message)
				self.the_net.Nodes[message.fromNode].informed.add(message.toNode)

			self.turns_elapsed += 1		
			
