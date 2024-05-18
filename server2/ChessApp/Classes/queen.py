OCCUPIED = 1
FREE = 0
ISHERE = -1

class Queen:
    def __init__(self, N):
        self.N = N
        self.columns = [ISHERE] * self.N
        number_of_diagonals = 2 * self.N - 1
        self.diagonals1 = [FREE] * number_of_diagonals
        self.diagonals2 = [FREE] * number_of_diagonals
        self.solutions = []

    def run(self):
        self.calculate(0)

    def calculate(self, row):
        for column in range(self.N):
            if self.columns[column] >= 0:
                continue
            this_diag1 = row + column
            if self.diagonals1[this_diag1] == OCCUPIED:
                continue
            this_diag2 = self.N - 1 - row + column
            if self.diagonals2[this_diag2] == OCCUPIED:
                continue
            self.columns[column] = row
            self.diagonals1[this_diag1] = OCCUPIED
            self.diagonals2[this_diag2] = OCCUPIED
            if row == self.N - 1:
                self.solutions.append(self.columns.copy())
            else:
                self.calculate(row + 1)
            self.columns[column] = ISHERE
            self.diagonals1[this_diag1] = FREE
            self.diagonals2[this_diag2] = FREE