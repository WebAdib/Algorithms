import collections

def bfs_shortest_path(graph, start, end):
    # Check if the start and end nodes are present in the graph
    if start not in graph or end not in graph:
        return None  # One or both of the nodes are not in the graph

    # Initialize a set to keep track of visited nodes
    visited = set()
    # Initialize a queue with the starting node and its path length (initialized to 0)
    queue = collections.deque([(start, 0)])

    # Perform BFS traversal
    while queue:
        # Dequeue a node and its path length from the front of the queue
        node, path = queue.popleft()
        visited.add(node)

        # Check if the current node is the destination
        if node == end:
            return path  # Return the shortest distance if we've reached the end node

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Calculate the new path length and enqueue the neighbor
                new_path = path + 1
                queue.append((neighbor, new_path))

    return None  # If no path exists between start and end

# Example graph represented as a dictionary (adjacency list)
graph = {0: [1,2,3], 1: [0,2], 2: [0,1,4], 3: [0], 4:[2,5], 5:[4]}

# Get user input for the starting and ending nodes
start_node = int(input("Enter Starting Node : "))
end_node = int(input("Enter Ending Node : "))

# Find the shortest path using BFS
shortest_path = bfs_shortest_path(graph, start_node, end_node)

# Display the result
if shortest_path:
    print(f"Number of edges to traverse from {start_node} to {end_node}: {shortest_path}")
else:
    print(f"No path found from {start_node} to {end_node}")
