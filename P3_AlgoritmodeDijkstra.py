import heapq
import networkx as nx
import matplotlib.pyplot as plt
import time

# Grafo de ejemplo
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

def draw_graph(graph, shortest_paths=None, current_node=None):
    G = nx.DiGraph()
    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Resaltar los caminos más cortos si están definidos
    if shortest_paths and current_node:
        nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='orange', node_size=600)
        nx.draw_networkx_labels(G, pos, labels={current_node: current_node}, font_weight='bold')
    
    plt.show()
    time.sleep(1)  # Pausa para visualizar cada paso

def dijkstra_visual(graph, start):
    # Diccionario para almacenar las distancias mínimas desde el nodo inicial
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]  # (distancia acumulada, nodo actual)
    visited = set()

    draw_graph(graph, shortest_paths)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)
        draw_graph(graph, shortest_paths, current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    draw_graph(graph, shortest_paths)
    return shortest_paths

# Ejecutar con visualización
dijkstra_visual(graph, 'A')
