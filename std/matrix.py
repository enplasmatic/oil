# from std.oil import *
class Matrix2D():
    def __init__(self, rows, columns, prefilled=0):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        for _ in self.rows:
            self.matrix.append([prefilled]*self.columns)

    def assign(self, pos, val):
        self.matrix[pos[0]][pos[1]] = val
        
    def get(self):
        return self.matrix
    
    def new_dimensions(self, rows, columns, extra_prefill=0):
        self.old_matrix = self.matrix.copy()
        self.matrix = []
        for i in rows:
            l = []
            for j in columns:
                try:
                    l.append(self.old_matrix[i][j])
                except:
                    l.append(extra_prefill)
            self.matrix.append(l)

    def is_square(self):
        return (self.rows == self.columns)