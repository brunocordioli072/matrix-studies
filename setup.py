import json
import pandas as pd
from scipy.spatial import distance_matrix

with open("./resources/data.json", "r") as read_file:
    data = json.load(read_file)

vertices = data["vertices"]
cities = data["cities"]
df = pd.DataFrame(vertices, columns=['xcord', 'ycord'], index=cities)
result = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
print(result)