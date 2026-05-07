from display.display_tool import sorted_nodes, draw_trace_table
from algo.dijkstra import dijkstra

def plot_dijkstra_trace(graph, start):
    nodes = sorted_nodes(graph)
    _, _, trace = dijkstra(graph, start, return_trace=True)
    values = [[step["distances"][node] for node in nodes] for step in trace]
    row_labels = [step["step"] for step in trace]

    blue_cells = set()
    pink_cells = set()

    for row_index, step in enumerate(trace):
        blue_cells.update(
            (row_index, nodes.index(node))
            for node in step["updated"]
        )
        pink_cells.update(
            (row_index, nodes.index(node))
            for node in step["visited"]
        )

    return draw_trace_table(
        f"Dijkstra Algorithm Trace from {start}",
        nodes,
        row_labels,
        values,
        corner_label="S",
        blue_cells=blue_cells,
        pink_cells=pink_cells,
    )
