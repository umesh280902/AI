class Tree:
    def __init__(self, key):
        self.value = key
        self.children = []

    def add_child(self, child_key):
        child_node = Tree(child_key)
        self.children.append(child_node)
        return child_node

class UCSAlgo:
    def dfid(self, start, goal):
        depth = 0
        while True:
            result = self.dls(start, goal, depth)
            if result is not None:
                return result
            depth += 1

    def dls(self, current, goal, max_depth, path=None):
        if path is None:
            path = []
        return self._dls(current, goal, max_depth, path, 0)

    def _dls(self, current, goal, max_depth, path, depth):
        if depth > max_depth:
            return None
        path.append(current.value)
        print("Current Path:", "->".join(path))
        if current.value == goal:
            return path
        for child in current.children:
            result = self._dls(child, goal, max_depth, path.copy(), depth + 1)
            if result is not None:
                return result
        return None
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

    # Test DFS algorithm
    algo = UCSAlgo()
    
    # Test DFID
    goal_node = '5'
    print("Goal Path (DFID):", algo.dfid(root, goal_node))

    # Test DLS with a specific depth limit
    max_depth = 3
    print("Goal Path (DLS):", algo.dls(root, goal_node, max_depth))