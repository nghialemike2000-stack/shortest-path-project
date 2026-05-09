import heapq


def has_negative_edge(graph):
    for u in graph:
        for v in graph[u]:
            if graph[u][v] < 0:
                return True
    return False


def get_path_string(graph, previous, start, target, distances):
    """Constructs the format: a(0) -(2)-> b(2) -(1)-> e(3)"""
    if distances[target] == float('inf'):
        return f"{target}: Unreachable"
    
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = previous[curr]
    path.reverse()
    
    result = []
    for i in range(len(path)):
        node = path[i]
        dist_at_node = distances[node]
        if i == 0:
            result.append(f"{node}({dist_at_node})")
        else:
            prev_node = path[i-1]
            weight = graph[prev_node][node]
            result.append(f"-({weight})-> {node}({dist_at_node})")
            
    return " ".join(result)

def dijkstra(graph, start, return_trace=False, verbose=True):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    trace = []

    if return_trace:
        trace.append({
            "step": "Start", "current": None, "distances": distances.copy(),
            "predecessors": previous.copy(), "updated": {start}, "visited": visited.copy()
        })

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        updated_nodes = set()
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue

            new_dist = current_distance + weight
            old_dist = distances[neighbor]
            old_str = "infinity" if old_dist == float('inf') else str(old_dist)
            
            if verbose:
                # Relaxation check printing
                print(f"{current_node}({current_distance}) -({weight})-> {neighbor}: ", end="")
                print(f"min({new_dist}, {old_str}) -> ", end="")
                
                if new_dist < old_dist:
                    # Temporary update for path string construction
                    temp_prev = previous[neighbor]
                    previous[neighbor] = current_node
                    temp_dist = distances[neighbor]
                    distances[neighbor] = new_dist
                    
                    print(f"choose {new_dist} so it will be {get_path_string(graph, previous, start, neighbor, distances)}")
                    
                    # Keep these changes as they are the new best
                    updated_nodes.add(neighbor)
                    heapq.heappush(priority_queue, (new_dist, neighbor))
                else:
                    print(f"no update")

        visited.add(current_node)

        if return_trace:
            trace.append({
                "step": current_node, "current": current_node,
                "distances": distances.copy(), "predecessors": previous.copy(),
                "updated": updated_nodes, "visited": visited.copy()
            })

    if verbose:
        print("\n==============================")
        print("BEST PATHS FROM START:")
        print("==============================")
        for node in sorted(graph.keys()):
            if node != start:
                path_str = get_path_string(
                    graph,
                    previous,
                    start,
                    node,
                    distances
                )

                print(f"{start} -> {node}: {path_str}")
        
        print()

    return (distances, previous, trace) if return_trace else (distances, previous)