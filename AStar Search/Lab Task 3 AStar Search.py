def a_star_search_all_paths(adjacency_list, heuristics, start_node, goal_node):
    def dfs(current_node, current_path, g_cost, visited):
        if current_node == goal_node:
            all_paths.append((current_path[:], g_cost))
            return

        for neighbor, weight in adjacency_list.get(current_node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                current_path.append(neighbor)
                dfs(neighbor, current_path, g_cost + weight, visited)
                current_path.pop()
                visited.remove(neighbor)

    all_paths = []
    visited = [start_node]
    dfs(start_node, [start_node], 0, visited)

    if all_paths:
        min_cost = None
        min_path = None
        for path, cost in all_paths:
            if min_cost is None or cost < min_cost:
                min_cost = cost
                min_path = path
        return min_path, min_cost
    else:
        return None, None


adjacency_list = {
    'A': [('D', 3), ('B', 5), ('C', 8)],
    'D': [('A', 3), ('F', 7)],
    'B': [('A', 5), ('E', 2)],
    'C': [('A', 8), ('F', 3), ('E', 3)],
    'F': [('D', 7), ('C', 3), ('G', 1)],
    'E': [('B', 2), ('C', 3), ('H', 1)],
    'H': [('E', 1), ('G', 2)],
    'G': [('F', 1), ('H', 2)]
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
path, cost = a_star_search_all_paths(adjacency_list, heuristics, start, goal)

if path:
    print(f"Path found by A* Search: {path} with cost {cost}")
else:
    print("No path found")
