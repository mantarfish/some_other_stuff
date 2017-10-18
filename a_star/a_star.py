'''Breadth First Search'''
import collections
import numpy as np
import sys
import scipy
import scipy.ndimage


def create_obstacle(array, i=20):
    weights = [[2, 1, 2],
              [1, 10, 1],
              [2, 1, 2]]
    for a in range(i):
        con = scipy.ndimage.filters.convolve(array, weights = weights, mode='wrap')

        if a % 2 == 0:
            boolean = (con == 1) | (con >= 10) | (con == 2)
        else:
            boolean = (con == 1) | (con >= 10)

        array = np.array(np.int8(boolean))
    return array


def punch_holes(array):
    weights = [[1, 1, 2],
              [2, 10, 1],
              [1, 1, 1]]
    
    con = scipy.ndimage.filters.convolve(array, weights=weights, mode='wrap')
    boolean = con >= 14
    array[boolean] = 0
    return array



def to_char_array(array, n):
    '''public implementation for to_char'''
    
    size = n

    boolean = (array == '1')
    array[boolean] = '#'
    boolean = (array == '0')
    array[boolean] = '.'

    for e in range(size):
        sys.stdout.write('|')
        for f in range(size):
            sys.stdout.write(' ' + array[e, f])
        print('|')

'''
def to_char(graph):
    array = graph.nodes
    size = graph.n

    for e in range(size):
        sys.stdout.write('|')
        for f in range(size):
            if array[e, f] == 1:
                sys.stdout.write(' #')
            else:
                sys.stdout.write(' .')
        print('|')
'''


class Graph():
    '''a graph contains nodes, and edges connecting those nodes.
    edges contains a cost, and each nodes has a name'''

    def __init__(self, nodes, edges):
        '''edges is a dict with node as its key and a list
        of neighbors as its values'''
        self.nodes = nodes
        self.edges = collections.defaultdict(list)
        for edge in edges:
            self.edges[edge[0]].append(edge[1])

    def get_neighbors_passable(self, node):
        return self.get_neighbors(node)

    def get_neighbors(self, node):
        return self.edges[node]


class Grid2D():
    def __init__(self, n=5):
        self.n = n

        self.nodes = np.zeros((n, n))
        self.nodes[1:4, 1] = 1
        self.nodes[3, 2:4] = 1
        self.nodes[0:2, 3:5] = 1

        self.nodes = create_obstacle(self.nodes, self.n)
        self.nodes = punch_holes(self.nodes)

    def draw(self):
        to_char_array(self.nodes, self.n)


    def get_neighbors_passable(self, node):

        neighbors = self.get_neighbors(node)

        neighbors_passable = [n for n in neighbors if self.nodes[n[0], n[1]] == 0]
        return neighbors_passable
            

    def get_neighbors(self, node):
        u = node[0]
        v = node[1]

        neighbors = [(u, (v - 1) % self.n),
                     (u, (v + 1) % self.n), 
                     ((u - 1) % self.n, v), 
                     ((u + 1 )% self.n, v)]

        return neighbors


class BreadthFirstSearch():
    def __init__(self, graph, starting_node, method='bfs', end=(15, 15)):
        self.graph = graph
        self.starting_node = starting_node
        self.path = {}
        self.end = end
        self.bfs()
        
        
        
    def bfs(self):
        '''graph is a Graph object, and starting_node is a node in graph'''
        frontier = collections.deque()
        frontier.append(self.starting_node)
        self.path[self.starting_node] = self.starting_node

        while frontier:
            current = frontier.popleft()
            # print('visiting {}'.format(current))
            for next_node in self.graph.get_neighbors_passable(current):
                if next_node not in self.path:
                    frontier.append(next_node)
                    self.path[next_node] = current
                    if next_node == self.end:
                        return

    def greedy(self):
        pass


    def draw_path(self):
        array = self.graph.nodes
        array = array.astype(str)
        edge_case_v = 5*(self.graph.n-1)
        edge_case_h = self.graph.n-1
        self.char_dict = {5: '\u2193', 1: '\u2192', -5: '\u2191', 
                         -1: '\u2190', edge_case_v: '\u2191', edge_case_h: '\u2190', 
                         -edge_case_v: '\u2193', -edge_case_h: '\u2192'}

        direction =''
        for next_node, prev in self.path.items():
            sub = np.subtract(next_node, prev)
            if tuple(sub) == (0, 0):
                char = 'o'
            else:
                direction = 5*sub[0] + sub[1]
                char = self.char_dict[direction]

            array[next_node[0], next_node[1]] = char
            array[self.starting_node[0], self.starting_node[1]] = 'o'
        
        to_char_array(array, self.graph.n)


class PathFindingAgent():
    def __init__(self, graph, start=(0, 0), end=(10, 10)):
        self.start = start
        self.end = end
        self.graph = graph
        self.validate()
        self.nav = BreadthFirstSearch(self.graph, self.start, end=self.end)
        self.path = []
        
    
    def validate(self):
        if self.graph.nodes[self.end[0], self.end[1]] == 1:
            self.start=(0, 0)
            self.end=(10, 10)
            raise ValueError('either start or end is not passable')

    def get_path(self):

        # prev: closer to starting
        # next: closer to end goal
        path = []
        path.append(self.end)
        next_node = self.end
        while next_node != self.start:
            prev = self.nav.path[next_node]
            path.append(prev)
            next_node = prev

        self.path = path


    def draw_path(self):
        path = self.path
        array = self.graph.nodes.astype(str)
        for i in path:
            array[i[0], i[1]] = '\u25a0'

        to_char_array(array, self.graph.n)
        
    def step(self):
        pass
