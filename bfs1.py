import queue
class Tree:
    def __init__(self,key):
        self.key=key
        self.children=[]

    def add_children(self,child_key):
        child_node=Tree(child_key)
        self.children.append(child_node)
        return child_node

class UCSAlgo:
    def bfs(self,start,target):
        q=queue.Queue()
        q.put(start)
        visited=set()
        path=[]
        while not q.empty():
            current=q.get()
            visited.add(current.key)
            path.append(current.key)
            print('->'.join(path))
            if current.key == target:
                return True
            for child in current.children:
                if child.key not in visited:
                    q.put(child)
                    visited.add(child.key)
        return False
        
if __name__=="__main__":
    root=Tree('1')
    child_node1=root.add_children('2')
    child_node2=root.add_children('3')
    child_node3=child_node1.add_children('4')
    child_node4=child_node1.add_children('5')
    child_node5=child_node2.add_children('6')
    child_node6=child_node2.add_children('7')

    print(root.key)
    for child in root.children:
        print(child.key)
        for grandchild in child.children:
            print(grandchild.key) 
    
    
    algo=UCSAlgo()
    goal_node='7'
    print('Goal Reached:',algo.bfs(root,goal_node))
