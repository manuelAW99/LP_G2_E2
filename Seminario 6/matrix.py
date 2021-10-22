class matrix:
    def __init__(self, rows:int = 0, columns:int = 0, initial = 0):
        if rows <= 0:
            raise Exception("The number of rows must be positive")
        if columns <= 0:
            raise Exception("The number of columns must be positive")
        
        self._rows = rows
        self._colums = columns
        self._type = type(initial)
        self._matrix = [[initial for i in range(columns)] for j in range(rows)]
    
    def GetRows(self):
        return self._rows
    
    def GetColumns(self):
        return self._colums
    
    def __iter__(self):
        return matrix_iter(self)
       
    def __add__(self, o):
        if not isinstance(o, matrix):
            raise Exception("You are not adding two matrices")
        if self.GetRows() != o.GetRows():
            raise Exception("The number of rows does not match")
        if self.GetColumns() != o.GetColumns():
            raise Exception("The number of columns does not match")

        sum_matrix = matrix(self.GetRows(),self.GetColumns())
        

    def __eq__(self, o):
        NotImplemented
    
    def __str__(self):
        string = ""
        for i in range(self.GetRows()):
            for j in range(self.GetColumns()):
                if j == 0:
                    string += '['
                string += str(self._matrix[i][j])
                if j != self.GetColumns() - 1: string += ', '
                else: string += ']\n'
        return string
        
class matrix_iter:
    def __init__(self, matrix):
        self._matrix = matrix
        self._current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current < self._matrix.GetRows() * self._matrix.GetColumns():
            row = self._current % self._matrix.GetRows()
            column = self._current % self._matrix.GetColumns()
            value = self._matrix._matrix[row][column]
            self._current += 1
            return value
        else:
            self._current = 0
            raise StopIteration("There are no more items in the matrix")
        
a = matrix(2,2, 0)
c = 0
for i in a:
    for j in a:
        c+=1
        print (c,i,j)
print(str(a))