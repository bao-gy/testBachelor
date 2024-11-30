import heapq

def dijkstra(graph, start):
    # Initialisierung: Distanzen zu allen Knoten auf unendlich setzen
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Überspringe, wenn wir bereits eine bessere Distanz gefunden haben
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Wenn ein kürzerer Weg gefunden wird, aktualisiere die Distanz
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Beispiel-Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}
start_node = 'A'
print(dijkstra(graph, start_node))
