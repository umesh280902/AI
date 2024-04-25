class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

def gbfs(start,target):
    queue=[start]
    path=[]
    while queue:
        print("Queue",[(node.name,node.value) for node in queue])
        current_node=queue.pop(0)
        path.append((current_node.name,current_node.value))
        if current_node.name==target:
            break
        if current_node.children:
            queue=sorted(queue+current_node.children,key=lambda x:x.value)
        print('Path:',path)
    return path

def create_sample_tree():
    a=Node('a',366)
    s=Node('s',253)
    f=Node('f',176)
    t=Node('t',329)
    z=Node('z',380)
    o=Node('o',374)
    r=Node('r',193)
    b=Node('b',0)
    a.children=[s,t,z]
    s.children=[f,o,r]
    f.children=[b]
    t.children=[]
    z.children=[]
    o.children=[]
    r.children=[]
    b.children=[]
    return a

if __name__=="__main__":
    root=create_sample_tree()
    start_node=root
    goal_node='b'
    path=gbfs(start_node,goal_node)
    print(f"Path to reach from '{start_node.name}' to '{goal_node}' is {path}")