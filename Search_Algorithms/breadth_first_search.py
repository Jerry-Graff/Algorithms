from collections import deque


def breadth_first_search(graph, start):
    """
    Performs Breadth-First Search on a graph starting from the start node.

    Args:
        graph (dict): Adjacency list representation of the graph where
                      graph[node] is a list of neighbors of node.
        start (any): The starting node for BFS traversal.

    Returns:
        list: A list of nodes in the order they were visited.

        Time Complexity: O(V + E)
        Space Complexity O(V)
    """

    visited = set()  # Keeps track of visited noded
    traveral_order = []  # Record the order
    queue = deque([start])  # Initialize queue with starting node

    visited.add(start)  # Marks start node as visited

    while queue:
        node = queue.popleft()  # Dequeue next node
        traveral_order.append(node)  # Process current node

        # Enqueue all unvisited nodes
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return traveral_order


def bfs_with_levels(graph, start):
    """
    Performs Breadth-First Search on a graph starting from the start node,
    printing the nodes level by level.

    Args:
        graph (dict): Adjacency list representation of the graph.
        start (any): Starting node for BFS.
    """
    visited = set([start])
    queue = deque([start])
    level = 0

    while queue:
        level_size = len(queue)    # Number of nodes at the current level
        print(f"Level {level}: ", end="")

        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            print(node, end=" ")  # Print the current node as part of this level

            # Enqueue all unvisited neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()  # Newline after finishing the current level
        level += 1


if __name__ == "__main__":
    # Define a graph using an adjacency list representation
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    order = breadth_first_search(graph, start_node)
    print(f"BFS Traversal starting from {start_node}: {order}")

    bfs_with_levels(graph, 'A')
