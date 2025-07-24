def bfs(graph, start, goal=None):  # assigning the goal to None as a default value in the function incase user does not assign any goal node and only want bfs traversal
    visited = [] # List to keep track of visited nodes to avoid revisiting
    queue = [start]  # Queue to manage the order of nodes to visit
    path_dict = {start: [start]}  # Dictionary to store the path to each node. but here list of list can be also used
    bfs_traversal = []   # List to store the BFS traversal order

    for node in queue:

        if node == goal:
            return bfs_traversal, path_dict[node]

        if node not in visited:
            visited.append(node)  # Mark the node as visited
            bfs_traversal.append(node)   # Add the node to the BFS traversal order

            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)   # Only add neighbors to the queue if they haven't been visited or aren't already in the queue
                    path_dict[neighbor] = path_dict[node] + [neighbor]  # Update path for neighbor

    return bfs_traversal, None  # Return traversal order and None if goal is not reached


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C', 'P'],
    'P': ['G'],
    'H': ['D']
}

bfs_traversal, shortest_path = bfs(graph, 'A', 'H')  # here if goal node is not declared, function will still work

print("BFS Traversal Order:", bfs_traversal)

if shortest_path:
    print(f"The shortest path from A to H is: {shortest_path}")
else:
    print("No path found to the goal.")