import random
from collections import namedtuple

from numpy.random import permutation

City = namedtuple("City", ["x", "y"])


def pairwise(iterable):
    iterable = list(iterable)
    return zip(iterable, iterable[1:] + iterable[:1])


def random_interval(individual):
    i, j = random.sample(range(len(individual)), k=2)
    i, j = min(i, j), max(i, j)
    return i, j


def random_population(population_size, num_genes):
    return [list(permutation(range(num_genes))) for _ in range(population_size)]


def read_input(path):
    cities = []
    with open(path, "r") as input_file:
        for line in input_file:
            x, y = line.split(" ")
            city = City(float(x), float(y))
            cities.append(city)
    return cities
