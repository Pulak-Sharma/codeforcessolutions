class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(result)

    def __sub__(self, other):
        result = [[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(result)

    def __mul__(self, other):
        result = [[sum(a*b for a, b in zip(row, col)) for col in zip(*other.data)] for row in self.data]
        return Matrix(result)

    def display(self):
        for row in self.data:
            print(row)

# Example usage:
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("Addition:")
(m1 + m2).display()
print("Subtraction:")
(m1 - m2).display()
print("Multiplication:")
(m1 * m2).display()