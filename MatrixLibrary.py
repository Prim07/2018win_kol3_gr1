class Matrix:
    def __init__(self, *values):
        valuesCount = len(values)
        self.matrixSize = int(valuesCount ** (1/2))
        isValidLength = (valuesCount ** (1/2)).is_integer()

        if not isValidLength:
            print("You passed wrong count of values")
            return

        self.matrix = []
        for i in range(self.matrixSize):
            self.matrix.append([x for x in values[i * self.matrixSize:(i+1) * self.matrixSize]])

    def add(self, otherMatrix):
        if self.matrixSize != otherMatrix.matrixSize:
            print("Matrixes has different sizes")
            return None
        newMatrixList = []
        for i in range(otherMatrix.matrixSize):
            for j in range(otherMatrix.matrixSize):
                newMatrixList.append(self.matrix[i][j] + otherMatrix.matrix[i][j])

        return Matrix(*newMatrixList)