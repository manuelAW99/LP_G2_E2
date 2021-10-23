
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
    
    def Transpose(self):
        transpose = matrix(self.GetColumns(), self.GetRows())
        transpose._matrix = [
            [self._matrix[i][j] for i in range(self.GetColumns())] 
            for j in range(self.GetRows())]
        return transpose

    # Operators   
    def __add__(self, o):
        if not isinstance(o, matrix):
            raise Exception("Both items must be matrices")
        if self.GetRows() != o.GetRows():
            raise Exception("The number of rows does not match")
        if self.GetColumns() != o.GetColumns():
            raise Exception("The number of columns does not match")

        sum_matrix = matrix(self.GetRows(),self.GetColumns())
        sum_matrix._matrix = [
            [(self._matrix[i][j] + o._matrix[i][j]) for j in range(self.GetColumns())] 
            for i in range(self.GetRows())]
        return sum_matrix

    def __sub__(self, o):
        neg = matrix(self.GetRows(), self.GetColumns())
        neg._matrix = [
            [(-1 * o._matrix[i][j]) for j in range(self.GetColumns())] 
            for i in range(self.GetRows())]
        return self + neg
    
    def __mul__(self, o):
        if not isinstance(o, matrix):
            raise Exception("Both items must be matrices")
        if self.GetColumns() != o.GetRows():
            raise Exception("The matrices cannot be multiplied(check the dimensions)")
        
        mul = matrix(self.GetRows(), o.GetColumns())
        for i in range(mul.GetRows()):
            for j in range(mul.GetColumns()):
                c = [o[k, j] for k in range(o.GetRows())]
                r = [self[i, k] for k in range(self.GetColumns())]

                value = 0
                for k in range(self.GetColumns()):
                    value += c[k] * r[k]
                mul[i, j] = value
        
        return mul

    # Comparators
    def __eq__(self, o):
        if not isinstance(o, matrix):
            raise Exception("Both items must be matrices")
        if self.GetRows() != o.GetRows() or self.GetColumns() != o.GetColumns():
            return False
        
        for i in range(self.GetRows()):
            for j in range(self.GetColumns()):
                if self._matrix[i][j] != o._matrix[i][j]:
                    return False
        return True

    def __ne__(self, o):
        return not self == o


    # Containers
    def __iter__(self):
        return matrix_iter(self)
    
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
    
    def __len__(self):
       return self.GetRows() * self.GetColumns()

    def __contains__(self, item):
        if not isinstance(item, self._type):
            raise Exception("The element must the same type of the matrix'elements")
        
        contains = False
        for i in self:
            if i == item:
                contains = True
                break
        return contains

    
    def __getitem__(self, item):
        if len(item) == 2:
            if not isinstance(item[0], int) or not isinstance(item[1], int):
                raise Exception("The index must be integers")
            if item[0] < 0 or item[0] >= self.GetRows() or item[1] < 0 or item[1] >= self.GetColumns():
                raise Exception("Index out of range") 
            return self._matrix[item[0]][item[1]]

        raise Exception("Incorrect indexing(check numbers of index or type)")
    
    def __setitem__(self, item, value):
        if len(item) == 2:
            if not isinstance(item[0], int) or not isinstance(item[1], int):
                raise Exception("The index must be integers")
            if item[0] < 0 or item[0] >= self.GetRows() or item[1] < 0 or item[1] >= self.GetColumns():
                raise Exception("Index out of range") 
            if self._type != type(value):
                raise Exception("Diferents types")
            self._matrix[item[0]][item[1]] = value
            return

        raise Exception("Incorrect indexing(check numbers of index or type)")
    
    # Attributes
    def __getattr__(self, item):
        inpt = item.split("_")[1:]

        try: index = [int(i) for i in inpt]
        except: raise Exception("The index must be integers")       
        return self[index]
    
       
class matrix_iter:
    def __init__(self, matrix):
        self._matrix = matrix
        self._current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current < self._matrix.GetRows() * self._matrix.GetColumns():
            row = self._current // self._matrix.GetColumns()
            column = self._current % self._matrix.GetColumns()
            value = self._matrix._matrix[row][column]
            self._current += 1
            return value
        else:
            self._current = 0
            raise StopIteration("There are no more items in the matrix")


a = matrix(3, 3, 0)
a[0,0]=1
a[0,1]=2
a[0,2]=3
a[1,0]=3
a[1,1]=1
a[1,2]=1
a[2,0]=5
a[2,1]=2
a[2,2]=1
print(a)

b = matrix(3, 3, 0)
b[0,0]=1
b[1,1]=1
b[2,2]=1
#b[0,1]=5
#b[1,0]=2
#b[2,0]=6
#b[2,1]=1
print(b)

print(a*b)
print(3 in a)