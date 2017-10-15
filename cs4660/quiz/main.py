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
    
    #Get neighbor room id from source node
#     neighbor_room_id = []
#     for n in empty_room['neighbors']:
#         n_ids = [n['id']]
#         neighbor_room_id.append(n_ids)

# print(neighbor_room_id)

def return_path(any_node,parents,edge_to):
    path = []
    while any_node in parents:
        path.append(edge_to[any_node])
        any_node = parents[any_node]
    path.reverse()
    return path

def  final_path(path,start):
    previous_node_id = start
    total = 0
    for p in path:
        previous_node = get_state(previous_node_id)
        next_node_id = p['id']
        total += p['event']['effect']
        print ("%s(%s):%s(%s): %i" % (previous_node['location']['name'], previous_node_id, p['action'], p['id'], p['event']['effect']))
        previous_node_id = next_node_id
    print("\nTotalHP: %i \n" % total)


def bfs(initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    
    q = [initial_node]
    visited_nodes = [initial_node['id']]
    parents = {}
    edge_to = {}
    while q:
        node = q.pop(0)
        for other_node in node['neighbors']:
            x = get_state(other_node['id'])
            edge = transition_state(node['id'],x['id'])
            if x['id'] == dest_node['id']:
                visited_nodes.append(x['id'])
                parents[x['id']] = node['id']
                edge_to[x['id']] = edge
                path = return_path(dest_node['id'],parents,edge_to)
                final_path(path,initial_node['id'])
                return 
            elif x['id'] not in visited_nodes:
                visited_nodes.append(x['id'])
                parents[x['id']] = node['id']
                edge_to[x['id']] = edge
                q.append(x)
            else:
                continue


def Dijkstra_search(initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    q = []
    q.append((0, initial_node))
    parents = {}
    distance = {initial_node: 0}
    edge_to = {}
    visited = []
    while len(q) > 0:
        node =get_state(q.pop()[1])
        visited.append(node['id'])
        for child in node['neighbors']:
            edge = transition_state(node['id'], child['id'])
            weight = distance[node['id']] + int(edge['event']['effect'])
            if child['id'] not in visited and (child['id'] not in distance or weight > distance[child['id']]):
                if child['id'] in distance:
                    q.remove((distance[child['id']], child['id']))
                q.append((weight, child['id']))
                distance[child['id']] = weight
                parents[child['id']] = node['id']
                edge_to[child['id']] = edge
        q = sorted(q, key=lambda x:x[0])
    path = return_path(dest_node, parents, edge_to)
    final_path(path, initial_node)

def extract_min(q, distance):
    minimum = q[0]
    for node in q:
        if distance[node['id']] < distance[minimum['id']]:
            minimum = node
    q.remove(minimum)
    return minimum


if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    dest_room = get_state('f1f131f647621a4be7c71292e79613f9')

    bfs(empty_room, dest_room)
    
    start_node = '7f3dc077574c013d98b2de8f735058b4'
    end_node = 'f1f131f647621a4be7c71292e79613f9'
    
    Dijkstra_search(start_node, end_node)

    #print(empty_room)
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))