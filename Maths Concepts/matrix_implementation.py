import numpy as np

class MatrixOperation:
    def __init__(self, mat_a, mat_b):
        self.mat_a = mat_a
        self.mat_b = mat_b

    def _check_row_elements(self, matrix):
        cols = len(matrix[0])
        for row in matrix:
            if len(row) != cols:
                raise ValueError("All rows must have equal number of elements")
        return True

    def _check_matrix_shape_for_multiplication(self):
        if self._check_row_elements(self.mat_a) and self._check_row_elements(self.mat_b):
            if len(self.mat_a[0]) == len(self.mat_b):
                return True
            else:
                raise ValueError("Matrix multiplication not possible")
        
    def _check_matrix_shape_for_addition(self):
        if self._check_row_elements(self.mat_a) and self._check_row_elements(self.mat_b):
            if (len(self.mat_a) == len(self.mat_b)) and (len(self.mat_a[0]) == len(self.mat_b[0])):
                return True
            else:
                raise ValueError("Matrix addition not possible")
            
    def add(self):
        if self._check_matrix_shape_for_addition():
            rows, cols = len(self.mat_a), len(self.mat_a[0])
            c = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    c[i][j] = self.mat_a[i][j] + self.mat_b[i][j]
            return c
        
    def multiply(self):
        if self._check_matrix_shape_for_multiplication():
            result = [[0 for _ in range(len(self.mat_b[0]))] for _ in range(len(self.mat_a))]
            for i in range(len(self.mat_a)):
                for j in range(len(self.mat_b[0])):
                    for k in range(len(self.mat_b)):
                        result[i][j] += self.mat_a[i][k] * self.mat_b[k][j]
            return result

    def transpose(self, matrix="a"):
        mat = self.mat_a if matrix == "a" else self.mat_b
        return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

    def determinant(self, matrix="a"):
        mat = self.mat_a if matrix == "a" else self.mat_b
        if len(mat) == 2 and len(mat[0]) == 2:
            return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        else:
            raise NotImplementedError("Only 2x2 determinant supported")


class MatrixOperationNumpy:
    def __init__(self, mat_numpy_a, mat_numpy_b):
        self.mat_numpy_a = np.array(mat_numpy_a)
        self.mat_numpy_b = np.array(mat_numpy_b)

    def add(self):
        return np.add(self.mat_numpy_a, self.mat_numpy_b)

    def multiply(self):
        return np.dot(self.mat_numpy_a, self.mat_numpy_b)

    def transpose(self, matrix="a"):
        mat = self.mat_numpy_a if matrix == "a" else self.mat_numpy_b
        return np.transpose(mat)

    def determinant(self, matrix="a"):
        mat = self.mat_numpy_a if matrix == "a" else self.mat_numpy_b
        return np.linalg.det(mat)


# Test
Mat = MatrixOperation([[1,2],[3,4]], [[5,6],[7,8]])
print("Manual Addition:", Mat.add())
print("Manual Multiplication:", Mat.multiply())
print("Manual Transpose A:", Mat.transpose("a"))
print("Manual Determinant A:", Mat.determinant("a"))

print("-"*60)

Mat_numpy = MatrixOperationNumpy([[1,2],[3,4]], [[5,6],[7,8]])
print("NumPy Addition:\n", Mat_numpy.add())
print("NumPy Multiplication:\n", Mat_numpy.multiply())
print("NumPy Transpose A:\n", Mat_numpy.transpose("a"))
print("NumPy Determinant A:", Mat_numpy.determinant("a"))
