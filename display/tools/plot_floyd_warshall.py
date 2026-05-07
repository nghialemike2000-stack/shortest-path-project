from display.display_tool import sorted_nodes, draw_trace_table
from algo.floyd_warshall import floyd_warshall

def plot_floyd_warshall_trace(graph):
    nodes = sorted_nodes(graph)
    _, negative_cycle, trace = floyd_warshall(graph, return_trace=True)
    diagonal_cells = {(index, index) for index in range(len(nodes))}

    for step in trace:
        label = step["label"]
        matrix = step["distances"]
        values = [
            [matrix[source][target] for target in nodes]
            for source in nodes
        ]
        blue_cells = {
            (nodes.index(source), nodes.index(target))
            for source, target in step["updated"]
        }

        draw_trace_table(
            f"Floyd-Warshall L({label})",
            nodes,
            nodes,
            values,
            corner_label="From / To",
            blue_cells=blue_cells,
            pink_cells=diagonal_cells,
            width_per_col=0.58,
            height_per_row=0.32,
        )

    print(f"Negative cycle: {negative_cycle}")
