import math

class Node:
	def __init__(self, value, i,a,b):
		self.left = None
		self.right = None
		self.n = 0
		self.value = value
		self.longest = []
		self.i = i
		self.a = a
		self.b = b
	def getLongestSubstringSize(self,i,j):
		return len(self.getLongestSubstring(i,j))

	def getLongestSubstring(self,i,j):
		l,r=[],[]
		if self.left:
			l = self.left.getLongestSubstring(i,j)
		if self.right:
			r = self.right.getLongestSubstring(i,j)

		if i==self.a and j==self.b:
			return self.longest
		elif i <= self.a <= self.b <= (i+j)/2:
			return l 
		elif math.ceil((i+j)/2) <= self.a <= self.b <= j:
			return r 
		elif i <= math.floor((self.a+self.b)/2) <= math.floor((self.a+self.b)/2)+1 <= j and i<=self.a:
			if self.left == None and self.right == None:
				return []
			return self.longest + l + r
		return l+r


	def count(self, i, j):
		l = 0
		r = 0
		if self.left:
			l = self.left.count(i,j)
		if self.right:
			r = self.right.count(i,j)
		elif i <= self.a <= self.b <= (i+j)/2:
			return l 
		elif math.ceil((i+j)/2) <= self.a <= self.b <= j:
			return r
		if i <= math.floor((self.a+self.b)/2) <= math.floor((self.a+self.b)/2)+1 <= j and i<=self.a:
			if self.left == None and self.right == None:
				p = self.parenthesized(self.value)
				if p[0]==True:
					self.longest = p[1]
				return self.n 
			p=self.parenthesized(self.value)
			if p[0] == True:
				self.n = self.n + len(p[1])
				self.longest = p[1]
			self.n += l+r
			return l + r
		else:
			return self.n

	def balanced(self,value):
		balanced = False
		stack = []
		n = 0
		caso = 0
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
					caso=1
					continue
				stack.pop()
		if -1 in stack:
			balanced = False

		if stack == [] and caso==0:
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

	def count_sublist(self,sublist,L):
		return len([None for i in range(len(L)) if L[i:i+len(sublist)]==sublist])

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
			counting = []
			for x in lists:
				if self.is_sublist(x,sel) and x in alreadyfound and counting[alreadyfound.index(x)][0] == counting[alreadyfound.index(x)][1]:
					nuevo.append(x)
				if self.is_sublist(x,sel) and x in alreadyfound:
					i = alreadyfound.index(x)
					counting[i][0]+=1
				if self.is_sublist(x,sel):
					alreadyfound.append(x)
					counting.append([1,self.count_sublist(x,sel)])
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


def createTree(S,i,j):
	mid = 2
	node = Node(S,mid,i,j)
	size = len(S)-1
	if S[0:mid] == [] or S[mid:size] == []:
		return node
	else:      
		node.add_left(createTree(S[0:mid],0,mid))
		node.add_right(createTree(S[mid:size],mid,size))
		return node

'''
La lista S que incluye la parentizacion debe tener la siguiente forma
S = ["(",")",")","(","("]
i representa el inicio del rango
j representa el final del rango
0<=i<=j<=len(S)-1
'''
def maxBP(S,i,j):
	if i<0 or (0<=i<j<len(S)) == False:
		print("Error en el rango elegido")
		return -1
	else:
		n = createTree(S,0,len(S)-1)
		n.count(i,j)
		print("Cadena original: ",S)
		print("Rango: ",S[i:j])
		print("La subcadena bien parentizada de longitud mayor es: ",n.getLongestSubstring(i,j))
		print("Longitud: ",n.getLongestSubstringSize(i,j))
		return n.getLongestSubstring(i,j)

def tests():
	pruebas = [["(",")",")","(","("],["(","(","(","(",")",")",")",")"], ["(",")","(","(",")",")",")"],
	["(","(",")"],[")",")",")",")"],["(",")","(","(",")","(",")",")"],["(",")","(","(",")","(",")","("]]
	resultados = [["(",")"],["(","(","(","(",")",")",")",")"], ["(",")","(","(",")",")"],
	["(",")"],[],["(",")","(","(",")","(",")",")"],["(",")","(",")","(",")"]]
	for x in range(len(pruebas)):
		a = maxBP(pruebas[x],0,len(pruebas[x])-1)
		print("Pass = ",a == resultados[x],"\n\n")
	pruebas2 = [["(",")",")","(","("], ["(",")","(","(",")",")",")"],["(",")","(","(",")","(",")",")"],
	["(",")","(","(",")","(",")","("]]
	resultados2 = [[],["(","(",")",")"],["(",")","(",")"],["(",")","(",")"]]
	for x in range(0,len(pruebas2)):
		a = maxBP(pruebas2[x],2,len(pruebas2[x])-2)
		print("Pass = ",a == resultados2[x],"\n\n")

tests()