def xorh(a, b):
    return a ^ b

def orh(a, b):
    return a | b

def andh(a, b):
    return a & b

def noth(a):
    return ~a

def righth(a):
    return a >> 1

def lefth(a):
    return a << 1

def nxorh(a, b):
    return noth(xorh(a, b))

def norh(a, b):
    return noth(orh(a, b))

def nandh(a, b):
    return noth(andh(a, b))

def binary(b):
    return bin(b)[2:]

def bitmask(array, length="dynamic"):
    if length == "dynamic": 
        length = len(array)
    subsets = []
    for val in range(0, 2**length):
        subset = []
        for i, bit in enumerate(reversed(binary(val))):
            if bit == "1":
                bit_on = array[-(i+1)]
                subset.append(bit_on)
        subsets.append(subset)
    return subsets

Fstar = 10 ** 9 + 7
def modF(val):
    return val % Fstar