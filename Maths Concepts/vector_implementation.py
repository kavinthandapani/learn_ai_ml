import numpy as np

class VectorOperations:
    def __init__(self, vector_a, vector_b):
        self.vector_a = vector_a
        self.vector_b = vector_b

    def _validate_lengths(self):
        if len(self.vector_a) != len(self.vector_b):
            raise ValueError("Vectors must have the same length")

    def add(self):
        self._validate_lengths()
        return [self.vector_a[i] + self.vector_b[i] for i in range(len(self.vector_a))]

    def subtraction(self):
        self._validate_lengths()
        return [self.vector_a[i] - self.vector_b[i] for i in range(len(self.vector_a))]

    def dot_product(self):
        self._validate_lengths()
        return sum(self.vector_a[i] * self.vector_b[i] for i in range(len(self.vector_a)))

    def magnitude(self, vector="a"):
        vec = self.vector_a if vector == "a" else self.vector_b
        return sum(x**2 for x in vec) ** 0.5


class VectorOperationsNumpy:
    def __init__(self, vec_a, vec_b):
        self.vec_a = np.array(vec_a)
        self.vec_b = np.array(vec_b)

    def add(self):
        return self.vec_a + self.vec_b
    
    def subraction(self):
        return self.vec_a - self.vec_b

    def dot_product(self):
        return np.dot(self.vec_a, self.vec_b)

    def magnitude(self, vector="a"):
        vec = self.vec_a if vector == "a" else self.vec_b
        return np.linalg.norm(vec)


if __name__ == "__main__":
    vector = VectorOperations([1, 2, 3], [4, 5, 6])
    print("Addition:", vector.add())
    print("Subtraction:", vector.subtraction())
    print("Dot Product:", vector.dot_product())
    print("Magnitude of vector A:", vector.magnitude("a"))
    print("Magnitude of vector B:", vector.magnitude("b"))

    vector_numpy = VectorOperationsNumpy([1, 2, 3], [4, 5, 6])
    print("Addition:", vector_numpy.add())
    print("Subtraction:", vector_numpy.subraction())
    print("Dot Product:", vector_numpy.dot_product())
    print("Magnitude of vector A:", vector_numpy.magnitude("a"))
    print("Magnitude of vector B:", vector_numpy.magnitude("b"))
    
