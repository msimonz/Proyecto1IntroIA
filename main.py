from grafo import Grafo

maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0]
]

G = Grafo.matrix_to_graph(maze)
print(Grafo.dfs(G, (0, 1)))
print(Grafo.bfs(G, (0, 1)))
Grafo.visualize_graph(G)

