class Array():
    def __init__(self, array):
        self.array = array

    def push_back(self, object):
        self.array.append(object)

    def insert(self, object, index):
        self.array.insert(index, object)

    def long(self):
        return len(self.array)
    
    def empty(self):
        self.array = []

    def reset(self, array):
        self.array = array

    def __call__(self):
        return self.array

    def __str__(self):
        return str(self.array)

class Frag():
    def __init__(self):
        self.vals = {}

    def set_to(self, arr):
        for i in arr:
            self.push(i)

    def push(self, val):
        if val in self.vals:
                self.vals[val] += 1
        else:
                self.vals[val] = 1

    def contains(self, val):
        return (val in self.vals)
        
    def count(self, val):
        return (self.vals[val])
    
    def remove(self, val):
         self.vals[val] -= 1
         if self.vals[val] <= 0:
            del self.vals[val]

    def remove_all(self, val):
        del self.vals[val]

    def collect_garbage(self):
         for val in self.vals:
              if self.vals[val] == 0:
                   del self.vals[val]
    
    def to_array(self):
        ans = []
        for i in self.vals:
             ans = ans + [i]*self.vals[i]
        return ans
    

class Double(float):
    def isdouble(self):
        return True