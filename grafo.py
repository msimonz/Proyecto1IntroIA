from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Grafo:
    def matrix_to_graph(matrix):
        rows, cols = len(matrix), len(matrix[0])
        G = nx.Graph()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    node = (r, c)
                    G.add_node(node)
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1:
                            neighbor = (nr, nc)
                            if neighbor not in G:
                                G.add_node(neighbor)
                            G.add_edge(node, neighbor)
        return G

    def dfs(grafo, start_node):
        visited = set()
        stack = [start_node]
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                stack.extend(neighbor for neighbor in grafo.neighbors(node) if neighbor not in visited)
        return order

    def bfs(grafo, start_node):
        visited = set()
        queue = deque([start_node])
        order = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                queue.extend(neighbor for neighbor in grafo.neighbors(node) if neighbor not in visited)
        return order

    def visualize_graph(G):
        pos = {(r, c): (c, -r) for r, c in G.nodes()}
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='b', alpha=0.7,
                font_size=10)
        plt.show()
