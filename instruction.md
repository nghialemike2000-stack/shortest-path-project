# Shortest Path Project Instructions

This file explains how to run the example algorithms in the repository and how the code is organized.

## 1. Repository structure

- `algo/`
  - `dijkstra.py` — Dijkstra algorithm for shortest paths.
  - `bellman_ford.py` — Bellman-Ford algorithm for shortest paths with negative weights.
  - `floyd_warshall.py` — Floyd-Warshall algorithm for all-pairs shortest distances.
- `graph/`
  - `graph3.py` — example graph data used by the notebook.
  - Other graph files are currently empty templates.
- `display/`
  - `display_tool.py` — drawing helpers for tables and visuals.
  - `display_graph3.ipynb` — notebook that renders trace tables for `GRAPH_3`.
  - `display_graph1.ipynb` through `display_graph6.ipynb` — notebooks for each graph exercise.

## 2. Graph format

Graphs are stored as nested Python dictionaries.

Example:

```python
GRAPH_3 = {
    'a': {'b': 2, 'c': 4, 'd': 1},
    'b': {'a': 2, 'c': 3, 'e': 1},
    # ...
}
```

- Outer keys are node names.
- Inner keys are neighbor nodes.
- Inner values are the edge weights.

## 3. GitHub repository URL

This project is hosted at:

https://github.com/nghialemike2000-stack/shortest-path-project

## 4. How to run the code locally

Use these commands from the repository root:

```powershell
cd "D:\Bách khoa\Math\Thầy Tuấn Anh\Shortest Path New"
python -c "from algo.dijkstra import dijkstra; from graph.graph3 import GRAPH_3; dist, prev = dijkstra(GRAPH_3, 'a'); print(dist); print(prev)"
```

If you clone the project from GitHub, run:

```powershell
git clone https://github.com/nghialemike2000-stack/shortest-path-project.git
cd shortest-path-project
python -c "from algo.dijkstra import dijkstra; from graph.graph3 import GRAPH_3; dist, prev = dijkstra(GRAPH_3, 'a'); print(dist); print(prev)"
```

## 5. Algorithm usage examples

### Dijkstra

```python
from algo.dijkstra import dijkstra
from graph.graph3 import GRAPH_3

distances, previous = dijkstra(GRAPH_3, 'a')
print(distances)
print(previous)
```

- Use Dijkstra when edge weights are all non-negative.

### Bellman-Ford

```python
from algo.bellman_ford import bellman_ford
from graph.graph3 import GRAPH_3

distances, previous, negative_cycle = bellman_ford(GRAPH_3, 'a')
print(distances)
print(previous)
print('negative cycle:', negative_cycle)
```

- Bellman-Ford works with negative edge weights.
- It also reports whether a negative cycle exists.

### Floyd-Warshall

```python
from algo.floyd_warshall import floyd_warshall
from graph.graph3 import GRAPH_3

distances, negative_cycle = floyd_warshall(GRAPH_3)
print(distances)
print('negative cycle:', negative_cycle)
```

- Floyd-Warshall computes distances between every pair of nodes.

## 6. How to use the notebooks

Open any notebook in `display/` and run each cell.

Use these notebooks for each graph exercise:

- `display_graph1.ipynb` for `graph.graph1`
- `display_graph2.ipynb` for `graph.graph2`
- `display_graph3.ipynb` for `graph.graph3`
- `display_graph4.ipynb` for `graph.graph4`
- `display_graph5.ipynb` for `graph.graph5`
- `display_graph6.ipynb` for `graph.graph6`

Each notebook imports its corresponding graph and then shows three sections:

- Dijkstra trace
- Bellman-Ford trace
- Floyd-Warshall trace

### How to edit graph data

Each `graph/graphX.py` file should define a dictionary named `GRAPH_X` using the same structure as `graph3.py`.

Example for `graph3.py`:

```python
GRAPH_3 = {
    'a': {'b': 2, 'c': 4, 'd': 1},
    'b': {'a': 2, 'c': 3, 'e': 1},
    'c': {'a': 4, 'b': 3, 'e': 2, 'f': 2},
    'd': {'a': 1, 'f': 5, 'g': 4},
    'e': {'b': 1, 'c': 2, 'h': 3},
    'f': {'c': 2, 'd': 5, 'g': 3, 'h': 3, 'i': 2, 'j': 4},
    'g': {'d': 4, 'f': 3, 'k': 2},
    'h': {'e': 3, 'f': 3, 'l': 1, 'o': 8},
    'i': {'f': 2, 'j': 3, 'l': 3, 'm': 2},
    'j': {'f': 4, 'i': 3, 'k': 6, 'm': 6, 'n': 3},
    'k': {'g': 2, 'j': 6, 'n': 4, 'r': 2},
    'l': {'h': 1, 'i': 3, 'm': 3, 'o': 6},
    'm': {'i': 2, 'j': 6, 'l': 3, 'n': 5, 'o': 4, 'p': 2},
    'n': {'j': 3, 'k': 4, 'm': 5, 'q': 2, 'r': 1},
    'o': {'h': 8, 'l': 6, 'm': 4, 'p': 2, 's': 6},
    'p': {'m': 2, 'o': 2, 'q': 1, 's': 2, 't': 1},
    'q': {'n': 2, 'p': 1, 'r': 8, 't': 3},
    'r': {'k': 2, 'n': 1, 'q': 8, 't': 5},
    's': {'o': 6, 'p': 2, 'z': 2},
    't': {'p': 1, 'q': 3, 'r': 5, 'z': 8},
    'z': {'s': 2, 't': 8}
}
```

Copy this style into `graph1.py` through `graph6.py`, updating the node names and weights for each graph exercise.

## 7. Notes for teammates

- `distances` shows the shortest distance values.
- `previous` stores the previous node for each path.
- In Floyd-Warshall, `distances[i][j]` is the shortest path from `i` to `j`.
- If a distance is `inf`, there is no path.

## 8. Optional: path reconstruction example

```python
from algo.dijkstra import dijkstra
from graph.graph3 import GRAPH_3

def build_path(prev, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    return list(reversed(path))


distances, previous = dijkstra(GRAPH_3, 'a')
print(build_path(previous, 'z'))
```

This builds the shortest path from `a` to `z`.
