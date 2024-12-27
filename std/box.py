class box():
    def __init__(self):
        self.vals = {}

    def manyset(self, lst):
        for value in lst:
            self.add(value)

    def add(self, val):
        if val in self.vals:
            self.vals[val] += 1
        else:
            self.vals[val] = 1

    def remove(self, val):
        if val in self.vals:
            self.vals[val] -= 1
            if self.vals[val] <= 0:
                del self.vals[val]
        else:
            raise ValueError(f"value {val} not in box")
        
    def removeall(self, val):
        if val in self.vals:
            del self.vals[val]
        else:
            raise ValueError(f"value {val} not in box")
        
    # def to_list(self):
    #     for i in self.

    def __repr__(self):
        return str(self.vals)
    
    def __call__(self):
        return self.vals
    

    def __add__(self,value):
        h = value().copy()
        for i in self.vals:
            if i in h:
                h[i] += self.vals[i]
            else:
                h[i] = self.vals[i]
        return h
    
    def __eq__(self, value):
        return self.vals == value.vals
    
    def __len__(self):
        return sum(self.vals.values())
    

    

    
myBox1 = box()
myBox1.manyset([3,5,3,3,3,2,5,3,6,4])
myBox2 = box()
myBox2.manyset([5,3,6,5,6,3,5])
print(len(myBox1))