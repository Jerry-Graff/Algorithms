import heapq
import math


def dijkstra(graph, start):
    """
    Computes the shortest paths from the start node to all other nodes in
    a weighted graph using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary representing the graph where graph[u] is a
                      list of (v, weight) pairs, indicating there is an edge
                      from u to v with the given weight.
        start (any): The starting node for computing shortest paths.

    Returns:
        dict: A dictionary of shortest distances from the start node to each
              other node. If a node is unreachable from the start, its
              distance will remain math.inf.
    """

    # Initialize distances to infinity for all nodes except the start node
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0  # Distance from start to itself is 0

    # Priority queue to select the next vertex with the smallest known distance
    # Each element in the priority queue is a tuple (distance, vertex)
    priority_queue = [(0, start)]

    while priority_queue:
        # Pop the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the distance in the queue is greater than the known shortest distance, skip processing
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight  # Calculate new distance to neighbor

            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Update the shortest distance to neighbor
                heapq.heappush(priority_queue, (distance, neighbor))  # Add neighbor to the queue for further exploration

    return distances


if __name__ == "__main__":
    # Define a weighted graph as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)
    print(f"Shortest paths from {start_vertex}: {shortest_paths}")