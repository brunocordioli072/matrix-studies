import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix

class MatrixUtils:
    def getDistanceMatrix(self, vertices):
        return distance_matrix(vertices, vertices)

    def getRoutingMatrix(self, matrix):

        v = len(matrix)
        p = np.zeros(matrix.shape)
        for i in range(0,v):
            for j in range(0,v):
                p[i,j] = i
                if (i != j and matrix[i,j] == 0): 
                    p[i,j] = -30000 
                    matrix[i,j] = 30000

        for k in range(0,v):
            for i in range(0,v):
                for j in range(0,v):
                    if matrix[i,j] > matrix[i,k] + matrix[k,j]:
                        matrix[i,j] = matrix[i,k] + matrix[k,j]
                        p[i,j] = p[k,j]
        return p
    
    def formatMatrix(self, matrix, index):
        return pd.DataFrame(matrix, index=index, columns=index)
