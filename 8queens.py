import random
import numpy as np

# 8 queens Problem...

# creating initial population ...
initialPopulation = []


def chromosomeGenerator():
    dummy = []
    for i in range(8):
        dummy.append(int(random.uniform(1, 9)))

    return dummy


def populationGenerator():
    for i in range(50):
        initialPopulation.append(chromosomeGenerator())


populationGenerator()


# print(initialPopulation)


# no of non-attacking pairs...
def fitnessFunction(chromosome):
    clashes = 0
    row_col_clashes = abs(len(chromosome) - len(np.unique(chromosome)))
    clashes += row_col_clashes

    # calculate diagonal clashes
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if i != j:
                dx = abs(i - j)
                dy = abs(chromosome[i] - chromosome[j])
                if dx == dy:
                    clashes += 1

    return 28 - clashes


# print(fitnessFunction([5, 2, 4, 7, 3, 8, 6, 1]))


def GA():
    k = 0
    while k < 500:
        RankedSolutions = []
        for j in initialPopulation:
            RankedSolutions.append((fitnessFunction(j), j))
        RankedSolutions.sort()
        RankedSolutions.reverse()

        # print(RankedSolutions)
        selectedSolutions = RankedSolutions[:4]
        # print(selectedSolutions)

        if RankedSolutions[0][0] == 28:
            print("Solution Found:", RankedSolutions[0])
            print("Gemerations: ", k)
            break

        # crossover
        el1 = selectedSolutions[0][1][:4]
        el2 = selectedSolutions[0][1][-4:]
        el3 = selectedSolutions[1][1][:4]
        el4 = selectedSolutions[1][1][-4:]
        el5 = selectedSolutions[2][1][:4]
        el6 = selectedSolutions[2][1][-4:]
        el7 = selectedSolutions[3][1][:4]
        el8 = selectedSolutions[3][1][-4:]

        newSol1 = el1 + el4
        newSol2 = el3 + el2
        newSol3 = el5 + el8
        newSol4 = el7 + el6

        index1 = int(random.uniform(0, 8))
        index2 = int(random.uniform(0, 8))
        index3 = int(random.uniform(0, 8))
        index4 = int(random.uniform(0, 8))
        # print(index1, index2)

        # mutation

        newSol1[index1] = int(random.uniform(1, 9))
        newSol2[index2] = int(random.uniform(1, 9))
        newSol3[index3] = int(random.uniform(1, 9))
        newSol4[index4] = int(random.uniform(1, 9))

        # print(newSol1, newSol2)
        unFitSolution = RankedSolutions[-4:]
        # print(unFitSolution)

        for i in range(len(initialPopulation)):
            if unFitSolution[0][1] == initialPopulation[i]:
                initialPopulation.remove(unFitSolution[0][1])
                initialPopulation.append(newSol1)
            if unFitSolution[1][1] == initialPopulation[i]:
                initialPopulation.remove(unFitSolution[1][1])
                initialPopulation.append(newSol2)
            if unFitSolution[2][1] == initialPopulation[i]:
                initialPopulation.remove(unFitSolution[2][1])
                initialPopulation.append(newSol3)
            if unFitSolution[3][1] == initialPopulation[i]:
                initialPopulation.remove(unFitSolution[3][1])
                initialPopulation.append(newSol4)

        k = k + 1


GA()
