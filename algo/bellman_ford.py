def bellman_ford(graph, start, return_trace=False):

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

    vertices = list(graph.keys())
    trace = []

    if return_trace:
        trace.append({
            "iteration": 0,
            "distances": distances.copy(),
            "updated": {start},
        })

    # Relax edges V-1 times
    for iteration in range(1, len(vertices)):

        updated = False
        updated_nodes = set()

        for u in graph:
            for v, weight in graph[u].items():

                if (
                    distances[u] != float('inf')
                    and distances[u] + weight < distances[v]
                ):

                    distances[v] = distances[u] + weight
                    previous[v] = u

                    updated = True
                    updated_nodes.add(v)

        if return_trace:
            trace.append({
                "iteration": iteration,
                "distances": distances.copy(),
                "updated": updated_nodes,
            })

        if not updated:
            break

    # Detect negative cycle
    negative_cycle = False

    for u in graph:
        for v, weight in graph[u].items():

            if (
                distances[u] != float('inf')
                and distances[u] + weight < distances[v]
            ):

                negative_cycle = True
                break

    if return_trace:
        return distances, previous, negative_cycle, trace

    return distances, previous, negative_cycle
