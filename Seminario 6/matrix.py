
class matrix:
    def __init__(self, rows:int = 0, columns:int = 0, initial = 0):
        if rows <= 0:
            raise Exception("The number of rows must be positive")
        if columns <= 0:
            raise Exception("The number of columns must be positive")
        
        self._rows = rows
        self._columns = columns
        self._initial = initial
        self._type = type(initial)
        self._matrix = [[initial for i in range(columns)] for j in range(rows)]
    
    def GetRows(self): return self._rows
    
    def GetColumns(self): return self._columns
    
    def IsSquare(self): return self._rows == self._columns
    
    def Clone(self):
        mclone = matrix(self.GetRows(), self.GetColumns(), self._initial)
        for i in range(mclone.GetRows()):
            for j in range(mclone.GetColumns()):
                mclone[i,j] = self[i,j]
        return mclone
    
    def Transpose(self):
        transpose = matrix(self.GetColumns(), self.GetRows(), self._initial)
        transpose._matrix = [
            [self._matrix[i][j] for i in range(self.GetColumns())] 
            for j in range(self.GetRows())]
        return transpose

    def AsType(self, ntype):
        nmatrix = matrix(self.GetRows(), self.GetColumns(), ntype(self._initial))
        for i in range(nmatrix.GetRows()):
            for j in range(nmatrix.GetColumns()):
                nmatrix[i,j] = ntype(self[i,j])
        return nmatrix
        
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
        neg = matrix(self.GetRows(), self.GetColumns(), o._initial)
        neg._matrix = [
            [(-1 * o._matrix[i][j]) for j in range(self.GetColumns())] 
            for i in range(self.GetRows())]
        return self + neg
    
    def __mul__(self, o):
        if not isinstance(o, matrix):
            if isinstance(o, self._type):
                mul = self.Clone()
                for i in range(self.GetRows()):
                    for j in range(self.GetColumns()):
                        mul[i,j] = self[i,j] * o
                return mul
            else: raise Exception("Both items must be matrices or a matrix and a scalar")
            
        elif self.GetColumns() != o.GetRows():
            raise Exception("The matrices cannot be multiplied(check the dimensions)")
        mul = matrix(self.GetRows(), o.GetColumns(), self._initial)
        for i in range(mul.GetRows()):
            for j in range(mul.GetColumns()):
                c = [o[k, j] for k in range(o.GetRows())]
                r = [self[i, k] for k in range(self.GetColumns())]
                value = 0
                for k in range(self.GetColumns()):
                    value += c[k] * r[k]
                mul[i, j] = value

        return mul

    def __truediv__(self, o):
        try:
            div = 1/o
        except: raise Exception("Is it not possible to divide by %s" %(str(o)))
        if isinstance(self._initial, float):
            return self * div
        else:
            return self.AsType(float) * div
    
    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise Exception("The exponent must be integer")
        if not self.IsSquare():
            raise Exception("Matrix most be square")
        if exponent > 0:
            mpow = self.Clone()
            for i in range(exponent - 1):
                mpow *= self
            return mpow
        else: raise Exception("The exponent must be positive")
    
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
    
    def __len__(self): return self.GetRows() * self.GetColumns()

    def __contains__(self, item):
        contains = False
        if isinstance(item, self._type):
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
            if type(self._initial) != type(value):
                raise Exception("Diferents types")
            self._matrix[item[0]][item[1]] = value
            return

        raise Exception("Incorrect indexing(check numbers of index or type)")
    
    # Attributes
    def __getattr__(self, item):
        inpt = item.split("_")

        if inpt[0] == 'as':
            try: 
                ntype = eval(inpt[1])
                return self.AsType(ntype)
            except: raise Exception("Undefined type: %s" %inpt[1])

        index = []
        try: index = [int(i) for i in inpt[1:]]
        except: raise Exception("The index must be integers")       
        return self[index]
    
    def __setattr__(self, name, value):
        inpt = name.split("_")[1:]
        try: 
            index = [int(i) for i in inpt]
            self[index] = value
        except: super().__setattr__(name, value)
        
    def __call__(self): return self

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


a = matrix(3, 3, .0)
a._0_0=11.0
a[0,1]=2.0
a[0,2]=3.0
a[1,0]=3.0
a[1,1]=1.0
a[1,2]=1.0
a[2,0]=5.0
a[2,1]=2.0
a[2,2]=1.0
print(a)
print(a._0_0)

b = matrix(3, 3)
b[0,0]=1
b[1,1]=1
b[2,2]=1
#b[0,1]=5
#b[1,0]=2
#b[2,0]=6
#b[2,1]=1
print(b)
#c = matrix(3,3,1.0)
print(a/2)
#print(3 in a)
#print(a**2)
#print(c*2.)
#print(c/2.)
print(a**2)
print(a.as_int()/6)
#print(a.as_intg())
print(a.as_int())