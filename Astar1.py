from queue import PriorityQueue

def astar(sample_tree,start,goal,heuristic):
    open_list=PriorityQueue()
    open_list.put((0,start))
    closed_list=set()
    while not open_list.empty():
        current_cost,current_node=open_list.get()
        if current_node==goal:
            print('Goal node reached')
            return
        closed_list.add(current_node)
        print('OPEN LIST:',list(open_list.queue))
        print('CURRENT:',current_node)
        print('CLOSED LIST:',closed_list)
        for neighbor,cost in sample_tree[current_node].items():
            if neighbor not in closed_list:
                new_cost=current_cost+cost
                open_list.put((new_cost+heuristic[neighbor],neighbor))
    print('Goal can\'t be reached')

sample_tree={
    'A':{'B':1,'C':2,'D':3},
    'B':{'E':4,'F':1},
    'C':{'G':2},
    'D':{'H':7},
    'E':{},
    'F':{},
    'G':{},
    'H':{},
}

heuiristic_tree={
    'A':13,'B':12,'C':20,'D':14,'E':12,'F':10,'G':9,'H':5
}
print("\nA* Algorithm with Sample Tree:")
astar(sample_tree, 'A', 'H', heuiristic_tree)