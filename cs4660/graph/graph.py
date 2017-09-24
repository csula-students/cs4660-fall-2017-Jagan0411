"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that graph object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """

    nodes = []
    edges = []

    f = open(file_path)
    node_info = f.readlines()
    #number of nodes
    size = int(node_info[0])

    #Storing node objects in list and referencing them later
    def getNodeData(data, nodes):
        for i in nodes:
            if i.data == data:
                return i
        return None
    
    for n in range(size):
        nodes.append(Node(n))

    #Parsing the input node data from file, adding edges and nodes later
    for d in range(1, len(node_info), 1):
        node_data = node_info[d].split(":")
        from_node = getNodeData(int(node_data[0]), nodes) #Node(int(node_data[0]))
        to_node = getNodeData(int(node_data[1]), nodes)   #Node(int(node_data[1]))   
        weight = int(node_data[2])
        edges.append(Edge(from_node, to_node, weight))
        # graph.add_node(from_node)
        # graph.add_node(to_node)
        #graph.add_edge(Edge(from_node, to_node, weight))

    #Adding edges and nodes here    
    for node in nodes:
        graph.add_node(node)
    for edge in edges:
        graph.add_edge(edge)

    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    #Checking the if node_2 is a value of key node_1    
    def adjacent(self, node_1, node_2):
        if node_2 in self.adjacency_list[node_1]:
            return True
        else:
            return False

    #Returning the values of that key node
    def neighbors(self, node):
        return self.adjacency_list[node]

    #Checking if node not available in Dic, adding the new key node later    
    def add_node(self, node):
        if node not in adjacency_list.keys():
            self.adjacency_list[node] = []
            return True

        else:
            return False
    
    #Checking if node exist in AL keys,removing the neighbors for that node and then removing the node itself             
    def remove_node(self, node):
        if node in self.adjacency_list.keys():
            for n in self.adjacency_list:
                if node in self.adjacency_list[n]:
                    self.adjacency_list[n].remove(node)
            del self.adjacency_list[node]
            return True
        else:
            return False

    #Checking if the edge already exist or if the node of that edge exist, if not then add the new edge        
    def add_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        if from_node not in self.adjacency_list.keys() or to_node not in self.adjacency_list.keys():
            return False
        elif to_node in self.adjacency_list[from_node]:
            return False
        else:
            self.adjacency_list[from_node].append(to_node)
            return True

    #Similar to add_edge, instead we remove the edge
    def remove_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        if from_node not in self.adjacency_list.keys() or to_node not in self.adjacency_list.keys():
            return False
        elif to_node not in self.adjacency_list[from_node]:
            return False
        else:
            self.adjacency_list[from_node].remove(to_node)
            return True

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    #Returning true or false for nodes that have an adjacent node, marked by weight
    def adjacent(self, node_1, node_2):
        return self.adjacency_matrix[self.__get_node_index(node_1)][self.__get_node_index(node_2)] > 0
 
    def neighbors(self, node):
        adj_node = self.adjacency_matrix[self.__get_node_index(node)]
        nodes = []
        for i in range(len(adj_node)):
            if adj_node[i] > 0:
                nodes.append(self.nodes[i])
        return nodes

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            for i in range(len(self.adjacency_matrix)):
                self.adjacency_matrix[i].append(0)
            add_row = []
            for j in range(len(self.adjacency_matrix) + 1):
                add_row.append(0)
            self.adjacency_matrix.append(add_row)
            return True

    #Removing the node and it's corresponding edges from the matrix
    def remove_node(self, node):
        if node not in self.nodes:
            return False
        else:
            node_index = self.__get_node_index(node)
            for i in self.adjacency_matrix:
                i.pop(node_index)
            self.adjacency_matrix.remove(self.adjacency_matrix[node_index])
            self.nodes.remove(node)
            return True

    #Checking if node for that exists, then add the edge for that node with it's weight
    def add_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        weight = edge.weight
        from_node_index = self.__get_node_index(from_node)
        to_node_index = self.__get_node_index(to_node)
        if to_node not in self.nodes or from_node not in self.nodes:
            return False
        elif self.adjacency_matrix[from_node_index][to_node_index] > 0:
            return False
        else:
            self.adjacency_matrix[from_node_index][to_node_index] = weight
            return True

    #Assigning 0 for removed edges for that node        
    def remove_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        from_node_index = self.__get_node_index(from_node)
        to_node_index = self.__get_node_index(to_node)
        if self.adjacency_matrix[from_node_index][to_node_index] > 0:
            self.adjacency_matrix[from_node_index][to_node_index] = 0
            return True
        else:
            return False

    """helper method to find node index"""   
    def __get_node_index(self, node):
        return self.nodes.index(node)

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    #Get the neighbours of the first node, check if the second node is present in it
    def adjacent(self, node_1, node_2):
        neighbor_nodes = self.neighbors(node_1)
        if node_2 in neighbor_nodes:
            return True
        else:
            return False

    #Check if the node has edges,add them to a list and return the nodes neighbouring to it
    def neighbors(self, node):
        neighbor_nodes = []
        for edge in self.edges:
            if edge.from_node == node:
                neighbor_nodes.append(edge.to_node)

        return neighbors

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    #Check if edges are there for that node, remove them and then remove the node
    def remove_node(self, node):
        for edge in self.edges:
            if edge.from_node == node or edge.to_node == node:
                self.edges.remove(edge)
        if node in self.nodes:
            self.nodes.remove(node)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        elif edge.from_node not in self.nodes or edge.to_node not in self.nodes:
            return False
        else:
            self.edges.append(edge)
            return True

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            return True
        else:
            return False