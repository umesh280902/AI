from queue import PriorityQueue

def astar(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0, start))
    closed_list = set()
    
    while not open_list.empty():
        current_cost, current_node = open_list.get()
        
        if current_node == goal:
            print("Goal node reached.")
            return
        
        closed_list.add(current_node)
        print("Current Node:", current_node)
        print("OPEN LIST:", list(open_list.queue))
        print("CLOSED LIST:", closed_list)
        
        for neighbor, cost in graph[current_node].items():
            if neighbor not in closed_list:
                new_cost = current_cost + cost
                open_list.put((new_cost + heuristic[neighbor], neighbor))
    
    print("Goal node not reachable from the starting node.")

# Define the sample tree as an adjacency list
sample_tree = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 2, 'E': 2},
    'C': {'F': 1},
    'D': {'G': 2},
    'E': {'H': 3},
    'F': {'I': 2},
    'G': {'J': 2},
    'H': {'K': 1},
    'I': {'L': 3},
    'J': {'M': 2},
    'K': {'N': 2},
    'L': {'O': 1},
    'M': {'P': 3},
    'N': {'Q': 2},
    'O': {'R': 2},
    'P': {'S': 1},
    'Q': {'T': 3},
    'R': {'U': 2},
    'S': {'V': 2},
    'T': {'W': 1},
    'U': {'X': 3},
    'V': {'Y': 2},
    'W': {'Z': 2},
    'X': {},
    'Y': {},
    'Z': {}
}

# Heuristic function for A* algorithm (Euclidean distance from node to goal)
heuristic_tree = {'A': 13, 'B': 12, 'C': 11, 'D': 10, 'E': 9, 'F': 8, 'G': 7, 'H': 6, 'I': 5, 'J': 4,
                  'K': 3, 'L': 2, 'M': 3, 'N': 4, 'O': 5, 'P': 6, 'Q': 7, 'R': 8, 'S': 9, 'T': 10,
                  'U': 11, 'V': 12, 'W': 13, 'X': 14, 'Y': 15, 'Z': 16}

# Test with the sample tree
print("\nA* Algorithm with Sample Tree:")
astar(sample_tree, 'A', 'Z', heuristic_tree)
