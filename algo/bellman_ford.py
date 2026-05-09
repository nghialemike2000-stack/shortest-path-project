def get_path_string(graph, previous, start, target, distances):
    """
    Constructs:
    a(0) -(2)-> b(2) -(1)-> e(3)
    """

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
            prev_node = path[i - 1]
            weight = graph[prev_node][node]

            result.append(
                f"-({weight})-> {node}({dist_at_node})"
            )

    return " ".join(result)


def has_negative_edge(graph):

    for u in graph:
        for v in graph[u]:

            if graph[u][v] < 0:
                return True

    return False


def bellman_ford(
    graph,
    start,
    return_trace=False,
    verbose=True
):

    # =========================================================
    # Validate start node
    # =========================================================

    if start not in graph:
        raise ValueError(
            f"Start node {start!r} is not in the graph."
        )

    # =========================================================
    # Initialize
    # =========================================================

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

    # =========================================================
    # Trace initialization
    # =========================================================

    if return_trace:

        trace.append({
            "iteration": 0,
            "distances": distances.copy(),
            "updated": {start},
        })

    # =========================================================
    # Print max iterations
    # =========================================================

    if verbose:

        print("=" * 60)
        print("BELLMAN-FORD ALGORITHM")
        print("=" * 60)

        print(
            f"Total vertices = {len(vertices)}"
        )

        print(
            f"Maximum iterations = V - 1 = {len(vertices)} - 1 = {len(vertices) - 1}"
        )

        # -----------------------------------------------------
        # Important theorem
        # -----------------------------------------------------

        if not has_negative_edge(graph):

            print(
                "\nGraph has NO negative edges."
            )

            print(
                "=> Negative cycle is impossible."
            )

    # =========================================================
    # Relax edges V-1 times
    # =========================================================

    for iteration in range(1, len(vertices)):

        updated = False
        updated_nodes = set()

        if verbose:

            print("\n" + "=" * 60)
            print(f"ITERATION {iteration}")
            print("=" * 60)

        for u in graph:

            for v, weight in graph[u].items():

                # ------------------------------------------------
                # Skip unreachable source
                # ------------------------------------------------

                if distances[u] == float('inf'):
                    continue

                old_distance = distances[v]
                new_distance = distances[u] + weight

                old_str = (
                    "inf"
                    if old_distance == float('inf')
                    else str(old_distance)
                )

                # ------------------------------------------------
                # Relaxation display
                # ------------------------------------------------

                if verbose:

                    print(
                        f"({u}, {v}) : "
                        f"{u}({distances[u]}) "
                        f"-({weight})-> {v} : "
                        f"min({new_distance}, {old_str})",
                        end=""
                    )

                # ------------------------------------------------
                # Relaxation condition
                # ------------------------------------------------

                if new_distance < old_distance:

                    distances[v] = new_distance
                    previous[v] = u

                    updated = True
                    updated_nodes.add(v)

                    if verbose:
                        print(" -> UPDATE")

                else:

                    if verbose:
                        print(" -> NO UPDATE")

        # =====================================================
        # Store trace
        # =====================================================

        if return_trace:

            trace.append({
                "iteration": iteration,
                "distances": distances.copy(),
                "updated": updated_nodes,
            })

        # =====================================================
        # Early stopping
        # =====================================================

        if not updated:

            if verbose:

                print("\nNo updates in this iteration.")

                print(
                    "=> Algorithm converged early."
                )

                print(
                    "=> Stop before reaching V-1 iterations."
                )

            break

    # =========================================================
    # Negative cycle detection
    # =========================================================

    negative_cycle = False

    for u in graph:

        for v, weight in graph[u].items():

            if (
                distances[u] != float('inf')
                and distances[u] + weight < distances[v]
            ):

                negative_cycle = True

                if verbose:

                    print("\nNegative cycle detected!")

                break

    # =========================================================
    # Final shortest paths
    # =========================================================

    if verbose:

        print("\n")
        print("=" * 60)
        print("BEST PATHS FROM START:")
        print("=" * 60)

        for node in sorted(graph.keys()):

            if node == start:
                continue

            path_str = get_path_string(
                graph,
                previous,
                start,
                node,
                distances
            )

            print(
                f"{start} -> {node}: {path_str}"
            )

    # =========================================================
    # Return
    # =========================================================

    if return_trace:

        return (
            distances,
            previous,
            negative_cycle,
            trace
        )

    return distances, previous, negative_cycle