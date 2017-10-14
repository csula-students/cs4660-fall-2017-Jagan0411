"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    #t_state = transition_state(empty_room['id'], empty_room['neighbors'][0]['id']
    
#path=return_path('7f3dc077574c013d98b2de8f735058b4','f1f131f647621a4be7c71292e79613f9')


    #Get neighbor room id from source node
    neighbor_room_id = []
    for n in empty_room['neighbors']:
        n_ids = [n['id']]
        neighbor_room_id.append(n_ids)

print(neighbor_room_id)



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

def bfs(initial_node, dest_node):
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
