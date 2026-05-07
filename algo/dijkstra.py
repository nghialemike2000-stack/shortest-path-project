import heapq


def has_negative_edge(graph):
    for u in graph:
        for v in graph[u]:
            if graph[u][v] < 0:
                return True
    return False


def dijkstra(graph, start, return_trace=False):

    if has_negative_edge(graph):
        raise ValueError(
            "Dijkstra cannot work with negative edge weights."
        )

    if start not in graph:
        raise ValueError(f"Start node {start!r} is not in the graph.")

    distances = {
        node: float('inf')
        for node in graph
    }

    previous = {
        node: None
        for node in graph
    }

    distances[start] = 0

    priority_queue = [(0, start)]
    visited = set()
    trace = []

    if return_trace:
        trace.append({
            "step": "Start",
            "current": None,
            "distances": distances.copy(),
            "updated": {start},
            "visited": visited.copy(),
        })

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node] or current_node in visited:
            continue

        visited.add(current_node)
        updated = set()

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node
                updated.add(neighbor)

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

        if return_trace:
            trace.append({
                "step": current_node,
                "current": current_node,
                "distances": distances.copy(),
                "updated": updated,
                "visited": visited.copy(),
            })

    if return_trace:
        return distances, previous, trace

    return distances, previous
