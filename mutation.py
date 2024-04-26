import random

def binaryChromosome(chromosome):
    return bin(chromosome)[2:].zfill(5)

def mutation(chromosome):
    mutationPoint=random.randint(0,4)
    print(mutationPoint)
    mutatedBit=1<<mutationPoint
    print(mutatedBit)
    mutatedChromosome=chromosome^mutatedBit
    return mutatedChromosome

def main():
    population=[random.randint(0,15) for _ in range(6)]
    mutationRate=0.1

    print('before mutation')
    for chromosome in population:
        print(f"{chromosome}:{binaryChromosome(chromosome)}")

    for i in range(len(population)):
        if random.random()<mutationRate:
            population[i]=mutation(population[i])

    print('after mutation')
    for chromosome in population:
        print(f"{chromosome}:{binaryChromosome(chromosome)}")


if __name__=="__main__":
    main()
