"""
Searches module defines all different search algorithms
"""


def return_path(graph, initial_node, dest_node, path, parents):
    if dest_node not in parents:
        return None
    if dest_node == initial_node:
        return path
    elif parents[dest_node] is None:
        return None
    else:
        path.insert(0, graph.get_edge(parents[dest_node], dest_node))
        return_path(graph, initial_node, parents[dest_node], path, parents)
        return path

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    
    q = [initial_node]
    visited_nodes = [initial_node]
    parents = {}
    while q:
        node = q.pop(0)
        for other_node in graph.neighbors(node):
            if other_node == dest_node:
                visited_nodes.append(other_node)
                parents[other_node] = node
                return return_path(graph, initial_node, dest_node, [], parents)
            elif other_node not in visited:
                visited_nodes.append(other_node)
                parents[other_node] = node
                q.append(other_node)
            else:
                continue

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
