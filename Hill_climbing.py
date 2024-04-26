import math
import random
from math import sin

def f1(x):
    return -(x**2)
def f2(x):
    return sin(x)
def f3(x):
    return -(5*x**2)+ (3*x) +2

def best_neighbour(f,x,step=0.1):
    if f(x-step)>f(x):
        return x-step
    elif f(x+step)>f(x):
        return x+step
    else:
        return x
    
def hillclimbing(f,x,max_iterations=1000):
    for _ in range(max_iterations):
        neighbour= best_neighbour(f,x)
        if f(neighbour)>f(x):
            x=neighbour
        else:
            break
        return x
    
if __name__=="__main__":
    ranges=[(-1,1),(-math.pi,math.pi),(-100,100)]
    functions=[f1,f2,f3]
    for i,f in enumerate(functions):
        x=random.uniform(*ranges[i])
        best_solution=hillclimbing(f,x)
        print(f"The best solution is found at {best_solution} with the value of {f(best_solution)}")