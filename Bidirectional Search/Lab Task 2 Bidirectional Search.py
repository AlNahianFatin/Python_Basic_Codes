def bidirect(graph, start, goal):
    def dfs(graph, current, goal, visited, path, cost):
        if current == goal:
            return path, cost

        visited.append(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                result = dfs(graph, neighbor, goal, visited, path + [neighbor], cost + weight)
                if result:
                    return result

        return None

    visited_start = []
    visited_goal = []

    path_start = []
    path_goal = []

    path_from_start = [start]
    path_from_goal = [goal]

    cost_start = 0
    cost_goal = 0

    while True:
        result_start = dfs(graph, start, goal, visited_start, path_from_start, cost_start)
        if result_start:
            path_start, cost_start = result_start
            break

        result_goal = dfs(graph, goal, start, visited_goal, path_from_goal, cost_goal)
        if result_goal:
            path_goal, cost_goal = result_goal
            break

    path_goal.reverse()
    final_path = path_start + path_goal

    return final_path, cost_start + cost_goal


graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('D', 3), ('E', 2), ('G', 4)],
    'D': [('A', 4), ('C', 3)],
    'E': [('C', 2), ('F', 1)],
    'F': [('E', 1), ('G', 3)],
    'G': [('C', 4), ('F', 3)]
}

start = 'A'
goal = 'D'

result = bidirect(graph, start, goal)
if result:
    print("Path found by Bidirectional Search using DFS:", result[0], "\nAnd the cost is:", result[1])
else:
    print("No path found")

