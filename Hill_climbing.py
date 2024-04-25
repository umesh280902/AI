import random

def objective_function(x):
    return (5*x**2)+3*x+2

def random_neighbours(current):
    return current+random.uniform(-0.5,0.5)

def hill_climbing(max_iterations):
    current_solution=random.uniform(-10,10)
    for _ in range(max_iterations):
        neighbour=random_neighbours(current_solution)
        if objective_function(neighbour)>objective_function(current_solution):
            current_solution=neighbour
        return current_solution
    
best_solution=hill_climbing(1000)
print('Best Solution Found',best_solution)
print('Objective Function value at the best solution',objective_function(best_solution))

