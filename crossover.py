import random

def binaryToDecimal(binary_str):
    return int(binary_str,2)

def decimalToBinary(chromsome):
    return bin(chromsome)[2:].zfill(5)

def crossover(population,crossoveRate):
    offspring=[]

    for i in range(0,len(population),2):
        parent1=population[i]
        parent2=population[i+1]

        if random.random()<crossoveRate*100:
            crossoverPoint=random.randint(1,len(parent1)-1)
            child1=parent1[:crossoverPoint]+parent2[crossoverPoint:]
            child2=parent2[:crossoverPoint]+parent1[crossoverPoint:]

            offspring.extend([child1,child2])
        else:
            offspring.extend([parent1,parent2])
        
    return offspring

pop=['13','10','7','9','5','16']
population=[bin(int(decimal))[2:].zfill(4) for decimal in pop]
print(population)

crossoverRate=0.25

print('Population before crossover')
for ind,binary in enumerate(population):
    print(f"Binary:{binary},Decinal:{binaryToDecimal(binary)}")

offSpring=crossover(population,crossoverRate)

print('Population after crossover')
for ind,binary in enumerate(offSpring):
    print(f"Binary:{binary},Decimal:{binaryToDecimal(binary)}")
