import math

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.n = 0
		self.value = value
		self.longest = None
	def getLongestSubstringSize(self):
		return (self.n+1)
	def getLongestSubstring(self):
		return self.longest
	def count(self):
		l = 0
		r = 0
		if self.left == None and self.right == None:
			p = self.parenthesized(self.value)
			if p[0]==True:
				self.longest = p[1]
			return self.n 
		if self.left:
			l = self.left.count()
		if self.right:
			r = self.right.count()
		p=self.parenthesized(self.value)
		if p[0] == True:
			self.n = self.n + 1
			self.longest = p[1]
		self.n += l+r
		return self.n

	def balanced(self,value):
		balanced = False
		stack = []
		n = 0
		if len(value) % 2 == 1:
			return balanced
		if "(" not in value or ")" not in value:
			return balanced

		for i in range(len(value)):
			x = value[i]
			if x == "(":
				stack.append(1)
			else:
				if stack == []:
					balanced = False
					continue
				stack.pop()
		if -1 in stack:
			balanced = False

		if stack == []:
			balanced = True
		else:
			balanced = False
		return balanced
				
	def sublists(self,lst):
		n = len(lst)
		sublists = []

		for start in range(n):
			for end in range(start + 1, n + 1):
				sublists.append(lst[start:end])

		return sublists

	def is_sublist(self, sublist, test_list):
		res = False
		for idx in range(len(test_list) - len(sublist) + 1):
		    if test_list[idx: idx + len(sublist)] == sublist:
		        res = True
		        break
		return res

	def parenthesized(self,value):
		wellparenthesized = False
		sublists = self.sublists(value)
		lists=[]
		for l in sublists:
			if self.balanced(l) == True:
				lists.append(l)
		maximum = 0
		sel = []
		for x in lists:
			if len(x) > maximum:
				maximum = len(x)
				sel = x
		nuevo = [sel]
		output=sel
		if sel != []:
			wellparenthesized = True
			lists.remove(sel)
			alreadyfound = []
			for x in lists:
				if self.is_sublist(x,sel) and x in alreadyfound:
					nuevo.append(x)
				if self.is_sublist(x,sel):
					alreadyfound.append(x)
			output = [x for xs in nuevo for x in xs]
		else:
			wellparenthesized = False
		return [wellparenthesized,output]

	def add_left(self,kid):
		self.left = kid
	def add_right(self,kid):
		self.right = kid
	def printTree(self):
		print(self.value)
		if self.left:
			self.left.printTree()
		if self.right:
			self.right.printTree()

def createTree(S):
	node = Node(S)
	mid = math.floor(len(S)/2)
	size = len(S)
	if S[0:mid] == [] or S[mid:size] == []:
		return node
	else:
		node.add_left(createTree(S[0:mid]))
		node.add_right(createTree(S[mid:size]))
		return node


def maxBP(S,i,j):
	if i<0 or (0<=i<j<len(S)) == False:
		print("Error en el rango elegido")
	else:
		n = createTree(S[i:j])
		n.count()
		print("Cadena original: ",S)
		print("Rango: ",S[i:j])
		print("La subcadena bien parentizada de longitud mayor es: ",n.getLongestSubstring())
		print("Longitud: ",n.getLongestSubstringSize())


S = ["(",")",")","(","(",")",")","(","(",")",")","("]
maxBP(S,3,10)
