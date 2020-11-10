import json
import pandas as pd
from core import MatrixUtils
from scipy.spatial import distance
import numpy as np
mu = MatrixUtils()
with open("./resources/data.json", "r") as read_file:
    data = json.load(read_file)

vertices = data["matrix"]
cities = data["cities"]

matrix = distance.cdist(vertices, vertices)
print("=============================================")
print("Distance Matrix Example: \n")
print(mu.formatMatrix(matrix, cities))
print("\n=============================================")

print("Routing Matrix: \n")
print("\nRouting Matrix Result: \n")
print(mu.formatMatrix(mu.getRoutingMatrix(matrix), cities))