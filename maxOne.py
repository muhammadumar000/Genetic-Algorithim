import random

# initial solution...

randArr = [1, 0]
initialPopulation = []


def populationGenerator():
    dummyArray = []
    for i in range(8):
        dummyArray.append(random.choice(randArr))
    return dummyArray


for s in range(6):
    initialPopulation.append(populationGenerator())


# print(initialPopulation)


# fitness function:
def fitnessFunction(chromosome):
    fitnessValue = 0
    for i in chromosome:
        if i == 1:
            fitnessValue += 1
    return fitnessValue


def GeneticAlgo():
    k = 0
    while True:
        RankedSolutions = []
        for j in initialPopulation:
            RankedSolutions.append((fitnessFunction(j), j))
        RankedSolutions.sort()
        RankedSolutions.reverse()

        # print(RankedSolutions)
        selectedSolutions = RankedSolutions[:2]
        # print(selectedSolutions)

        if RankedSolutions[0][0] == 8:
            print("Solution Found:", RankedSolutions[0])
            print("Gemerations: ", k)
            break
        # crossover
        el1 = selectedSolutions[0][1][:4]
        el2 = selectedSolutions[0][1][-4:]
        el3 = selectedSolutions[1][1][:4]
        el4 = selectedSolutions[1][1][-4:]

        newSol1 = el1 + el4
        newSol2 = el3 + el2

        index1 = int(random.uniform(0, 7))
        index2 = int(random.uniform(0, 7))
        # print(index1, index2)

        # mutation

        if newSol1[index1] == 0:
            newSol1[index1] = 1
        else:
            newSol1[index1] = 1
        if newSol2[index2] == 0:
            newSol2[index2] = 0
        else:
            newSol2[index2] = 0

        # print(newSol1, newSol2)
        unFitSolution = RankedSolutions[-2:]
        # print(unFitSolution)

        for i in range(len(initialPopulation)):
            if unFitSolution[0][1] == initialPopulation[i]:
                initialPopulation.remove(unFitSolution[0][1])
                initialPopulation.append(newSol1)
            if unFitSolution[1][1] == initialPopulation[i]:
                initialPopulation.remove(unFitSolution[1][1])
                initialPopulation.append(newSol2)


        k = k + 1


GeneticAlgo()
