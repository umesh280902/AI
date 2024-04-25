import queue

class Tree:
    def __init__(self, key):
        self.value = key
        self.children = []

    def add_child(self, child_key):
        child_node = Tree(child_key)
        self.children.append(child_node)
        return child_node

class UCSAlgo:
    def bfs(self, start, goal):
        q = queue.Queue()
        q.put(start)
        visited = set()
        path=[]
        while not q.empty():
            current = q.get()
            visited.add(current.value)
            path.append(current.value)
            print("->".join(path))
            if current.value == goal:
                return True
            for child in current.children:
                if child.value not in visited:
                    q.put(child)
                    visited.add(child.value)
        return False
    
if __name__ == "__main__":
    root = Tree('1')
    child_node1 = root.add_child('2')
    child_node2 = root.add_child('3')

    child_node3 = child_node1.add_child('4')
    child_node4 = child_node1.add_child('5')

    child_node5 = child_node2.add_child('6')
    child_node6 = child_node2.add_child('7')

    print(root.value)
    for child in root.children:
        print(child.value)
        for grandchildren in child.children:
            print(grandchildren.value)

    # Test BFS algorithm
    algo = UCSAlgo()
    goal_node = '7'
    print("Goal Reached:", algo.bfs(root, goal_node))
