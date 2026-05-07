from pathlib import Path
import sys

import matplotlib.pyplot as plt

project_root = Path.cwd()
if project_root.name == "display":
    project_root = project_root.parent

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from algo.bellman_ford import bellman_ford
from algo.dijkstra import dijkstra
from algo.floyd_warshall import floyd_warshall


START = "a"
INF = float("inf")


def sorted_nodes(graph):
    return sorted(graph)


def value_text(value):
    if value == INF:
        return chr(8734)
    return str(value)


def draw_trace_table(
    title,
    column_labels,
    row_labels,
    values,
    corner_label,
    blue_cells=None,
    green_cells=None,
    pink_cells=None,
    width_per_col=0.68,
    height_per_row=0.36,
):
    blue_cells = blue_cells or set()
    green_cells = green_cells or set()
    pink_cells = pink_cells or set()

    headers = [corner_label] + list(column_labels)
    table_rows = [
        [row_label] + [value_text(value) for value in row]
        for row_label, row in zip(row_labels, values)
    ]

    fig_width = max(8, width_per_col * len(headers))
    fig_height = max(3.2, height_per_row * (len(row_labels) + 2))
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.set_title(title, fontsize=18, fontweight="bold", pad=20)
    ax.axis("off")

    table = ax.table(
        cellText=table_rows,
        colLabels=headers,
        cellLoc="center",
        loc="center",
    )

    small_table = len(headers) > 14 or len(row_labels) > 14
    table.auto_set_font_size(False)
    table.set_fontsize(8 if small_table else 12)
    table.scale(1, 1.35 if small_table else 1.5)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#222222")
        cell.set_linewidth(1.0)

        if row == 0:
            cell.set_facecolor("#d9d9d9")
            cell.get_text().set_fontweight("bold")
            continue

        if col == 0:
            cell.set_facecolor("#f1f1f1")
            continue

        key = (row - 1, col - 1)
        if key in pink_cells:
            cell.set_facecolor("#ffc7c7")
            cell.get_text().set_color("#ff1f1f")
        elif key in blue_cells:
            cell.set_facecolor("#cfe8ff")
            cell.get_text().set_color("#001fff")
            cell.get_text().set_fontweight("bold")
        elif key in green_cells:
            cell.set_facecolor("#cfffd0")
            cell.get_text().set_color("#087b14")
            cell.get_text().set_fontweight("bold")

    fig.tight_layout()
    plt.show()
    return fig
