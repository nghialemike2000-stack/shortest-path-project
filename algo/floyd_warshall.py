from copy import deepcopy


def floyd_warshall(graph, return_trace=False):

    nodes = list(graph.keys())

    dist = {
        i: {
            j: float('inf')
            for j in nodes
        }
        for i in nodes
    }

    # Distance to itself = 0
    for node in nodes:
        dist[node][node] = 0

    # Fill graph weights
    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight

    trace = []

    if return_trace:
        trace.append({
            "label": "0",
            "middle": None,
            "distances": deepcopy(dist),
            "updated": set(),
        })

    # Floyd-Warshall
    for k in nodes:
        updated_nodes = set()

        for i in nodes:
            for j in nodes:

                if (
                    dist[i][k] != float('inf')
                    and dist[k][j] != float('inf')
                ):

                    new_distance = dist[i][k] + dist[k][j]

                    if new_distance < dist[i][j]:
                        dist[i][j] = new_distance
                        updated_nodes.add((i, j))

        if return_trace:
            trace.append({
                "label": k,
                "middle": k,
                "distances": deepcopy(dist),
                "updated": updated_nodes,
            })

    # Negative cycle detection
    negative_cycle = False

    for node in nodes:
        if dist[node][node] < 0:
            negative_cycle = True

    if return_trace:
        return dist, negative_cycle, trace

    return dist, negative_cycle
