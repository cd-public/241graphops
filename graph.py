# graph.py 

class Graph:

	def __init__(self):
		self.setv = []
		self.sete = []
		
	def addEdge(self,v1,v2,e,c):
		self.sete.append(self.Edge(e,v1,v2,c))
		
	def addVertex(self,n):
		new = self.Vertex(n)
		if new not in self.setv:
			self.setv.append(new)

	def getVertex(self,n):
		names = [[v.name,v] for v in self.setv]
		for i in names:
			if i[0] == n:
				return i[1]
		
	def fromCSV(self,file):  
		for line in open(file,"r"):
			[v1,v2,e,c] = line[:-1].split(", ")
			self.addVertex(v1)
			self.addVertex(v2)
			self.addEdge(self.getVertex(v1),self.getVertex(v2),e,c)

	def allPaths(self):
		news = [[e] for e in self.sete]
		pths = [news]
		hops = 0
		while news:
			news = []
			for p in pths[hops]:
				for e in self.sete:
					intr = p[-1].vrts.intersection(e.vrts)
					if len(intr) == 1:
						if not any([e.vrts.intersection(e2.vrts) for e2 in p[:-1]]):
							news.append(p + [e])
			if news:
				hops, pths = hops + 1, pths + [news]
		return [p for ps in pths for p in ps]
		
	def pathFrom(self,p):
		if len(p) == 1:
			return p[0].vrts
		return p[0].vrts.union(p[-1].vrts) - p[1].vrts.union(p[-2].vrts)

	class Vertex: # vertexes

		def __repr__(self):
			return "VERTEX: " + self.name
		def __str__(self):
			return "VERTEX: " + self.name
		def __eq__(self,other):
			return self.name == other.name

		def __init__(self, n):
			self.name = str(n)
			
		def __hash__(self):
			return hash(self.__str__())
			
	class Edge: # edges

		def __repr__(self):
			lst = list(self.vrts)
			return "EDGE: " + self.name + " from " + str(lst[0]) + " to " + str(lst[1])
		def __str__(self):
			return self.__repr__()

		def __init__(self, n, v1, v2, c):
			self.name = n
			self.vrts = set([v1,v2])
			self.cost = c
			
		def __hash__(self):
			return hash(self.__str__())