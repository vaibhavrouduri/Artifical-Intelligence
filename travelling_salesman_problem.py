# -*- coding: utf-8 -*-
"""Travelling_Salesman_Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NQZdziiJabJu67PXpua7yQ5-GAqDKsV9
"""

import random
import numpy as np
import math
import matplotlib.pyplot as plt
import time

"""Pairwise distances between 14 cities. 100 signifies that the 2 cities are not connected"""

distances = [[0,100,100,100,100,100,0.15,100,100,0.2,100,0.12,100,100],
		        [100,0,100,100,100,100,100,0.19,0.4,100,100,100,100,0.13],
	        	[100,100,0,0.6,0.22,0.4,100,100,0.2,100,100,100,100,100],
		        [100,100,0.6,0,100,0.21,100,100,100,100,0.3,100,100,100],
		        [100,100,0.22,100,0,100,100,100,0.18,100,100,100,100,100],
		        [100,100,0.4,0.21,100,0,100,100,100,100,0.37,0.6,0.26,0.9],
		        [0.15,100,100,100,100,100,0,100,100,100,0.55,0.18,100,100],
		        [100,0.19,100,100,100,100,100,0,100,0.56,100,100,100,0.17],
		        [100,0.4,0.2,100,0.18,100,100,100,0,100,100,100,100,0.6],
		        [0.2,100,100,100,100,100,100,0.56,100,0,100,0.16,100,0.5],
		        [100,100,100,0.3,100,0.37,0.55,100,100,100,0,100,0.24,100],
		        [0.12,100,100,100,100,0.6,0.18,100,100,0.16,100,0,0.4,100],
		        [100,100,100,100,100,0.26,100,100,100,100,0.24,0.4,0,100],
		        [100,0.13,100,100,100,0.9,100,0.17,0.6,0.5,100,100,100,0]]

"""Fitness is defined as the inverse of the cumulative sum of distances of a current state"""

def fitnessFunction2(state_in_population):
  sum = 0
  for i in range(len(state_in_population) - 1):
    sum += distances[state_in_population[i]][state_in_population[i + 1]]
  sum += distances[state_in_population[0]][state_in_population[13]]

  return 1/sum

"""Function to select a member of the population with probablilty of being selected directly proportional to fitness value"""

def randomSelection2(population):
  fitness = []
  for i in population:
    fitness.append(fitnessFunction2(i))
  x = random.choices(population, weights = (i for i in fitness), k = 1)
  return x[0]

"""Selecting the best child out of 2 children of 2 parents"""

def reproduce2(x, y):
  x1 = x.copy()
  y1 = y.copy()
  x2 = x.copy()
  y2 = y.copy()
  child1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  child2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  left = random.randint(0, len(x))
  right = random.randint(left, len(x))
  z = x1[left:right]
  for i in z:
    child1[x1.index(i)] = i
    y1.remove(i)
  child1 = y1[0:left] + z + y1[left:]
  w = y2[left:right]
  for i in w:
    child2[y2.index(i)] = i
    x2.remove(i)
  child2 = x2[0:left] + w + x2[left:] 
  if fitnessFunction2(child1) >= fitnessFunction2(child2):
    return child1
  else:
    return child2

"""Generating a population of size 20 with initially all members of the population being identical"""

def generatePopulation2(state):
  population = []
  count = 20
  while count != 0:
    population.append(state)
    count -= 1
  return population

"""Exchanging the position of 2 pairs of cities in a state """

def mutate2(state):
  r1 = random.randint(0, 13)
  r2 = random.randint(0, 13)
  while r2 == r1:
    r2 = random.randint(0, 13)
  temp = state[r1]
  state[r1] = state[r2]
  state[r2] = temp
  r3 = random.randint(0, 13)
  r4 = random.randint(0, 13)
  while r4 == r3:
    r4 = random.randint(0, 13)
  temp = state[r3]
  state[r3] = state[r4]
  state[r4] = temp

  return state

def geneticAlgorithm2(population, fitnessFunction):
  start_time = time.time()
  performance = 0
  best_in_every_generation = []
  cost_in_every_generation = []
  generation_number = []
  while performance < 10000:
    new_population = []
    for i in range(len(population)):
      x = randomSelection2(population)    
      y = randomSelection2(population)
      child = reproduce2(x, y)
      if random.randint(1, 10) == 1:
        child = mutate2(child)
      new_population.append(child)
    population = new_population
    best = fitnessFunction(population[0])
    for i in population:
      if fitnessFunction(i) > best:
        best = fitnessFunction(i)
        ans = i
    best_in_current_generation = max(fitnessFunction(i) for i in population)
    best_in_every_generation.append(best_in_current_generation)
    cost_in_every_generation.append(1/best_in_current_generation)
    performance+=1
    generation_number.append(performance)
    
  #plt.plot(generation_number, best_in_every_generation)
  plt.plot(generation_number, cost_in_every_generation)
  for i in best_in_every_generation:
    print(i) 
  print(ans)
  end_time = time.time()
  return ans, end_time - start_time

geneticAlgorithm2(generatePopulation2([0,1,2,3,4,5,6,7,8,9,10,11,12,13]), fitnessFunction2)

