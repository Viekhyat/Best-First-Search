from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

def input_graph():
    graph = {}
    while True:
        node = input("Enter a node (or type 'done' to finish): ").strip().upper()
        if node == 'DONE':
            break
        neighbors = input(f"Enter neighbors for node {node} (comma-separated): ").strip().upper()
        neighbors_list = [n.strip() for n in neighbors.split(",")] if neighbors else []
        graph[node] = neighbors_list
    return graph

def draw_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)  # Layout for the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()
if __name__ == "__main__":
    print("Enter the graph structure:")
    graph = input_graph()
    start_node = input("Enter the starting node for BFS: ").strip().upper()
    bfs_result = bfs(graph, start_node)
    print("BFS traversal order:", bfs_result)
    draw_graph(graph)