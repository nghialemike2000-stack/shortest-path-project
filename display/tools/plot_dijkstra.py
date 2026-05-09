from display.display_tool import sorted_nodes, draw_trace_table
from algo.dijkstra import dijkstra

def plot_dijkstra_trace(graph, start):
    nodes = sorted_nodes(graph)
    # The print result happens inside this call:
    _, _, trace = dijkstra(graph, start, return_trace=True, verbose=True)
    
    values = []
    for step in trace:
        row = []
        for node in nodes:
            dist = step["distances"][node]
            parent = step["predecessors"][node]
            if dist == float('inf'):
                row.append(float('inf'))
            elif parent is None:
                row.append(f"{dist}")
            else:
                row.append(f"{dist} ({parent})")
        values.append(row)

    row_labels = [step["step"] for step in trace]
    blue_cells = set()
    pink_cells = set()

    for row_index, step in enumerate(trace):
        blue_cells.update((row_index, nodes.index(n)) for n in step["updated"])
        pink_cells.update((row_index, nodes.index(n)) for n in step["visited"])

    return draw_trace_table(
        f"Dijkstra Algorithm Trace from {start}",
        nodes, row_labels, values,
        corner_label="S", blue_cells=blue_cells, pink_cells=pink_cells,
    )
