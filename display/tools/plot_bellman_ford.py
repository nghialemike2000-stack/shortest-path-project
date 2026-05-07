from display.display_tool import sorted_nodes, draw_trace_table
from algo.bellman_ford import bellman_ford

def plot_bellman_ford_trace(graph, start):
    nodes = sorted_nodes(graph)
    _, _, negative_cycle, trace = bellman_ford(graph, start, return_trace=True)
    values = [[step["distances"][node] for node in nodes] for step in trace]
    row_labels = [step["iteration"] for step in trace]
    start_column = nodes.index(start)

    blue_cells = set()
    pink_cells = {
        (row_index, start_column)
        for row_index in range(len(trace))
    }

    for row_index, step in enumerate(trace):
        blue_cells.update(
            (row_index, nodes.index(node))
            for node in step["updated"]
        )

    figure = draw_trace_table(
        f"Bellman-Ford Algorithm Trace from {start}",
        nodes,
        row_labels,
        values,
        corner_label="Iteration",
        blue_cells=blue_cells,
        pink_cells=pink_cells,
    )

    print(f"Negative cycle: {negative_cycle}")
    return figure
