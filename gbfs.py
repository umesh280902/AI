class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

def greedy_bfs(root, goal_node):
    queue = [root]
    path = []
    while queue:
        print("Queue:", [(node.name, node.value) for node in queue])
        current_node = queue.pop(0)
        path.append((current_node.name, current_node.value))
        if current_node.name == goal_node:
            break
        if current_node.children:
            queue = sorted(queue + current_node.children, key=lambda x: x.value)
        print("Path:", path)
    return path

def main():
    start_node = input("Enter the start node: ")
    end_node = input("Enter the goal node: ")
    root = create_sample_tree()
    print("Greedy BFS traversal:")
    path = greedy_bfs(root, end_node)
    print("Start Node:", start_node)
    print("End Node:", end_node)
    print("Path:")
    for node in path:
        print("Node:", node[0], ", Value:", node[1])
        if node[0] == end_node:
            break

def create_sample_tree():
    # Create nodes
    a = Node('a', 40)
    b = Node('b', 32)
    c = Node('c', 25)
    d = Node('d', 35)
    e = Node('e', 19)
    f = Node('f', 17)
    g = Node('g', 0)
    h = Node('h', 10)
    # Assign children
    a.children = [b, c, d]
    b.children = [e]
    c.children = [e, f]
    d.children = [f]
    e.children = [h]
    f.children = [g]
    h.children = [g]
    return a  # Returning the root node

if __name__ == "__main__":
    main()
