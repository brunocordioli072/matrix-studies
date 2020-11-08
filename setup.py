import json
import pandas as pd
from core import MatrixUtils
from scipy.spatial import distance_matrix
import numpy as np
mu = MatrixUtils()

with open("./resources/random_vertices.json", "r") as read_file:
        data = json.load(read_file)

vertices = data["vertices"]
cities = data["cities"]
print("=============================================")
print("Distance Matrix Example: \n")
print(mu.formatMatrix(mu.getDistanceMatrix(vertices), cities))
print("\n=============================================")

with open("./resources/random_matrix.json", "r") as read_file:
        data = json.load(read_file)

rand_matrix = np.array(data["matrix"])
rand_index = data["cities"]

print("Routing Matrix: \n")
print("Existing Random Matrix: \n")
print(mu.formatMatrix(rand_matrix, rand_index))

print("\nRouting Matrix Result: \n")
print(mu.formatMatrix(mu.getRoutingMatrix(rand_matrix), rand_index))