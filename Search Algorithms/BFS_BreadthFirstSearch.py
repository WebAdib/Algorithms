# BFS algorithm in Python
import collections

# BFS algorithm
def bfs(graph, root):
    # Initialize a set to keep track of visited vertices
    visited = set()
    
    # Initialize a deque (double-ended queue) for BFS and enqueue the root
    queue = collections.deque([root])
    visited.add(root)

    # Iterate until the queue is empty
    while queue:
        # Dequeue a vertex from the front of the queue
        vertex = queue.popleft()
        # Print or process the current vertex
        print(str(vertex) + " ", end="")

        # Explore neighbors of the current vertex
        for neighbour in graph[vertex]:
            # If the neighbour has not been visited, mark it as visited and enqueue it
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Main function
if __name__ == '__main__':
    # Example graph represented as an adjacency list
    graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}

    # Print the BFS traversal starting from vertex 0
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
