def greedy_best_first_search(graph, start, goal, heuristics):
    queue = [(heuristics[start], start, [start])]
    visited = []

    while queue:
        min_index = 0
        for i in range(len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i

        current_node_data = queue.pop(min_index)
        heuristic, current_node, path = current_node_data

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.append(current_node)

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((heuristics[neighbor], neighbor, path + [neighbor]))

    return None


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'F'],
    'E': ['B', 'C', 'H'],
    'F': ['C', 'D', 'G'],
    'G': ['F', 'H'],
    'H': ['E', 'G']
}

heuristics = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

start = 'A'
goal = 'G'

result = greedy_best_first_search(graph, start, goal, heuristics)

if result:
    print("Path found by Greedy Best-First Search:", result)
else:
    print("No path found")