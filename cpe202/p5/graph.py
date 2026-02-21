from typing import List, Any

from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''Reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!

        self.graph = {}
        file = open(filename, 'r')
        for line in file:
            x = line.split()
            self.add_vertex(x[0])
            self.add_vertex(x[1])
            self.add_edge(x[0], x[1])
        file.close()

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if self.get_vertex(key) is None:
            new = Vertex(key)
            self.graph[new.id] = new

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        v1_obj = self.get_vertex(v1)
        v2_obj = self.get_vertex(v2)

        v1_obj.adjacent_to.append(v2)
        v2_obj.adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key in self.graph:  # O(1)
            return self.graph[key]
        return None

    def get_vertices(self):
        '''Returns a list of IDs representing the vertices in the graph, in ascending order'''
        lst = list(self.graph.keys())
        lst.sort()
        return lst

    def dfs(self, s, vertices):
        '''Returns a list of vertex IDs reachable from source s'''
        visited = {}
        for v in vertices:
            visited[v] = False  # initialize dictionary w all vertices set to False

        stack = Stack(10000)  # not sure if this is ideal size
        stack.push(s)

        while stack.size() > 0:
            top = stack.peek()
            stack.pop()
            if not visited.get(top):
                visited[top] = True
                for id in self.get_vertex(top).adjacent_to:
                    if not visited.get(id):
                        stack.push(id)
        return [k for k, v in visited.items() if v is True]

    def conn_components(self):
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item in each sublist.'''
        # This method MUST use Depth First Search logic!
        res = []
        vertices = self.get_vertices()

        while len(vertices) > 0:
            lst = self.dfs(vertices[0], vertices)
            lst.sort()
            res.append(lst)
            vertices = list(set(vertices) - set(lst))
        return res

    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        # This method MUST use Breadth First Search logic!
        vertices = self.get_vertices()
        q = Queue(len(vertices))
        colors = (set(), set())

        for id in vertices:
            if id in colors[0] or id in colors[1]:
                continue
            q.enqueue((id, 0))
            colors[0].add(id)
            while not q.is_empty():
                curr_id, curr_color = q.dequeue()
                other_color = (curr_color + 1) % 2  # either 0 or 1
                for adj_id in self.get_vertex(curr_id).adjacent_to:
                    if adj_id in colors[curr_color]:  # same color
                        return False
                    if adj_id in colors[other_color]:
                        continue
                    q.enqueue((adj_id, other_color))
                    colors[other_color].add(adj_id)
        return True