import random
#Objective function: maximize this function
def fitness(x):
    return x**2
#Create a random individual
def create_individual():
    return random.uniform(-10,10)
#Mutate an individual
def mutate(x):
    return x + random.uniform(-1,1)
#Crossover(averages two parents)
def crossover(x1,x2):
    return(x1+x2)/2
#Genetic Algorithm Solver
def genetic_algorithm(pop_size=10,generations=20):
    population=[create_individual() for _ in range(pop_size)]
    for gen in range(generations):
        #Evaluate fitness of each individual
        population= sorted(population,key=fitness, reverse=True)
        print(f"Generation{gen},Best Fitness:{fitness(population[0]):.2f}, Best x:{population[0]:.2f}")
        #Select top 50%
        survivors= population[:pop_size//2]
        #Reproduce to create new individuals
        children=[]
        while len(children)<pop_size//2:
            parent1= random.choice(survivors)
            parent2= random.choice(survivors)
            child= crossover(parent1, parent2)
            child= mutate(child)
            children.append(child)
        #Form the new generation
        population= survivors+children
#Run the algorithm
pop_size= int(input("Enter population size:"))
generations=int(input("Enter number of generations:"))
genetic_algorithm(pop_size, generations)