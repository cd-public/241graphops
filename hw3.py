# HW3: Graph Ops

# Intended to completed within graph.py (provided as-is).

# Problem 0: Connected Vertexes (20 pts)

# west.csv contains a number of cities in and around the Western United 
# States connected by the Interstate Highway System. However, not all major
# cities in and around this area are connected via roadways. Two major state
# capitols - Honolulu and Juneau - are not connected to each other or any other
# major city. This corresponds to the graph notion of connectivity - two 
# vertexes are *connected* if there exists some path between them.

# Write a method in the Graph class "areConnected(v0, v1)" that accepts two arguments,
# which must both be vertexes within the graph, and returns True if there 
# exists a path between these two vertexes and False otherwise.

# Keep in mind a vertex may be disconnected from another vertex will still
# having some connections. In and around the Southern United States, for 
# example, the cities of San Juan and Ponce, both in Puerto Rico, are 
# connected to each other by PR-52, but not connected to Miami by any roadway.

from graph import *

g = Graph()
g.fromCSV("west.csv")
cs = ["Honolulu", "Juneau"]
[g.addVertex(c) for c in cs]
vs = [g.getVertex(c) for c in cs + ["Seattle","Vancouver"]]
print(vs[0],"connect",vs[2],g.areConnected(vs[0],vs[2]), "should be", False)
print(vs[2],"connect",vs[3],g.areConnected(vs[2],vs[3]), "should be", True)

# Problem 1: Connected Graphs (20 pts)

# west.csv is an example of a connected graph, in that every vertex is 
# connected to every other vertex. However, adding Honolulu or Juneau
# vertexes would cause the graph to no longer be connected. 

# Write a method in the Graph class "isConnected()" that returns True if a 
# graph is connected and False otherwise.

g = Graph()
g.fromCSV("west.csv")
print("connected without AK/HI",g.isConnected(), "should be", True)
g.addVertex("Honolulu")
g.addVertex("Juneau")
print("connected with AK/HI",g.isConnected(), "should be", False)

# Problem 2: Sets of Vertexes (10 pts)

# *** YOU MAY WISH TO DO THIS FIRST ***

# graph.py uses many set operations to determine whether paths are valid,
# acyclic, or between any two given points. Many of these operations rely on
# constructed sets of vertexes from paths, which are lists of edges.

# Write a method in the Graph class "pathVertexes(p)" that accepts a path,
# which is a list of edges, and returns a set containing all vertexes in any
# edge within that path. This will represent all cities passed through by a
# path.

g = Graph()
g.fromCSV("west.csv")
p = g.sete[:5]
cs = ["Vancouver", "Seattle", "Portland", "San Francisco", "Los Angeles", "Tijuana"]
vs = set([g.getVertex(c) for c in cs])
print("vertex set test",g.pathVertexes(p) == vs, "should be", True)