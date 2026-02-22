from sys import argv
from stack_array import *

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is empty with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''

    even_vertices = vertices[1::2]  # global definitions
    odd_vertices = vertices[::2]

    class InDegreeAdjacent:  # class to hold in degree and adjacent vertices

        def __init__(self, vertex):
            self.vertex = vertex
            self.in_degree = 0
            self.adjacent = []

        def create(self, vertex, vertices):
            self.in_degree = even_vertices.count(vertex)  # in degree
            for i, v in enumerate(odd_vertices):  # adjacent vertices
                if v == self.vertex:
                    self.adjacent.append(even_vertices[i])
            
    if len(vertices) == 0:
        raise ValueError('input contains no edges')
    if len(vertices) % 2 != 0:
        raise ValueError('input contains an odd number of tokens')
    for i, v in enumerate(even_vertices):
        if v == odd_vertices[i]:  # a vertex cannot come before itself
            raise ValueError('input contains a cycle')

    pairs = []  # if two vertices point to each other
    for i, v in enumerate(odd_vertices):
        pairs.append([v, even_vertices[i]])
    for p in pairs:
        reverse = [p[1], p[0]]
        if reverse in pairs:
            raise ValueError('input contains a cycle')

    res = ''
    unique_vertices = []  # get all unique vertices
    for v in vertices:
        if v not in unique_vertices:
            unique_vertices.append(v)

    d = {}  # create dictionary
    for v in unique_vertices:
        obj = InDegreeAdjacent(v)
        obj.create(v, vertices)
        d[v] = [obj.in_degree, obj.adjacent]

    s = Stack(30) 
    for key in d:  # push all vertices w in degree of 0
        if d[key][0] == 0:
            s.push(key)

    while not s.is_empty(): 
        popped = s.peek()
        s.pop()
        res += popped
        res += '\n'

        for v in d[popped][1]:  # reduce in degree of adjacent vertices
            d[v][0] -= 1
            if d[v][0] == 0:
                s.push(v)

    if len(res) == 0 or len(res) == 2:  # not sure
        raise ValueError('input contains a cycle')

    return res

# 100% Code coverage NOT required
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG.  Use this code 
       if you want to run tests on a file with a list of edges'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()