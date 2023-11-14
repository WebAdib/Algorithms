def dfs(graph, start, visited=None):
    # If visited set is not provided, create an empty set to track visited vertices
    if visited is None:
        visited = set()
    
    # Mark the current vertex as visited
    visited.add(start)
    
    # Print or process the current vertex
    print(start, end=' ')
    
    # Recursively explore neighbors of the current vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            # Call DFS on the unvisited neighbor
            dfs(graph, neighbor, visited)

# Define the graph as a dictionary where the keys are vertices and the values are lists of neighboring vertices.
graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2, 5], 5: [4]}

# Example usage:
if __name__ == "__main__":
    # Print a message indicating the traversal type and starting vertex
    print("Depth-First Traversal (starting from vertex 0):")
    
    # Call the DFS function with the graph and starting vertex
    dfs(graph, 0)
