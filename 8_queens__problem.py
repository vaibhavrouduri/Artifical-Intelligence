# -*- coding: utf-8 -*-
"""8-Queens _Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jwqglBONvl75d9nUq1C7NJcJhgx6w9hB
"""

import random
import numpy as np
import math
import matplotlib.pyplot as plt
import time

"""Fitness Function defined as number of non-attacking queens + 1"""

def fitnessFunction1(state_in_population):
  x = state_in_population
  x_set = set(x)
  ans = 0
  for i in x_set:
    count = x.count(i)
    if count > 1:
      comb = int((math.factorial(count)/(2 * math.factorial(count - 2))))
      ans += int(comb)
  for i in x_set:
    for j in x_set:
      if x.index(i) == x.index(j):
        ans += 0
      else:
        if abs(i - j) == abs(x.index(i) - x.index(j)):
          ans += 0.5
  total = int((math.factorial(8)/(2 * math.factorial(8 - 2))))

  return 1 + total - int(ans)

"""Function to select a member of the population with probablilty of being selected directly proportional to fitness value"""

def randomSelection1(population):
  fitness = []
  for i in population:
    fitness.append(fitnessFunction1(i))
  x = random.choices(population, weights = (i for i in fitness), k = 1)
  return x[0]

"""Randomly changing the position of 2 queens"""

def mutate1(state):
  r1 = random.randint(0, 7)
  r2 = random.randint(0, 7)
  state[r1] = random.randint(1, 8)
  state[r2] = random.randint(1, 8)

  return state

"""Selecting the best child out of 2 children of 2 parents




"""

def reproduce1(x, y):
  n = len(x)
  c = random.randint(0, n - 1)
  z = x[:c]
  for i in y[c:n]:
    z.append(i)
  w = y[:c]
  for i in x[c:n]:
    w.append(i)
  if fitnessFunction1(z) >= fitnessFunction1(w):
    return z
  else:
    return w

"""Generating a population of size 20 with initially all members of the population being identical"""

def generatePopulation1(state):
  population = []
  count = 20
  while count != 0:
    population.append(state)
    count -= 1
  return population

"""Genetic Algorithm to solve the problem. Also prints a graph showing how the fitness value of each generation is progressing, number of generations required to reach a goal state and  time taken to reach a goal state"""

def geneticAlgorithm1(population, fitnessFunction):
  start_time = time.time()
  best = 0
  performance = 0
  best_in_every_generation = []
  generation_number = []
  while best < 29:
    new_population = []
    for i in range(len(population)):
      x = randomSelection1(population)    
      y = randomSelection1(population)
      child = reproduce1(x, y)
      if random.randint(1, 10) == 1:
        child = mutate1(child)
      new_population.append(child)
    population = new_population
    for i in population:
      if fitnessFunction(i) == 29:
        best = fitnessFunction(i)
        ans = i
    best_in_current_generation = max(fitnessFunction(i) for i in population)
    best_in_every_generation.append(best_in_current_generation)
    performance+=1
    generation_number.append(performance)
    
  plt.plot(generation_number, best_in_every_generation)
  print(performance) 
  end_time = time.time()
  return ans, end_time - start_time

geneticAlgorithm1(generatePopulation1([1,2,3,4,5,6,7,8]), fitnessFunction1)

