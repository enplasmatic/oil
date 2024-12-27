from bisect import *
from functools import cmp_to_key
from itertools import groupby
from itertools import permutations
# from std.oil import *

def Pair(x,y):
    return (x,y)

def Vector2d(x,y):
    return [x,y]

def Vector(x,y):
    return [x,y]

def Vector3d(x,y,z):
    return [x,y,z]

def Segment(x,y):
    return set([x,y])

def reflex(array):
    return array


def sortall(array):
    return sorted(array)

def sortby(array, byfunc, byreverse=True):
    return sorted(array, key=byfunc, reverse=byreverse)

def sortcomp(array, byfunc, byreverse=True):
    return sorted(array, key=cmp_to_key(byfunc), reverse=byreverse)
    
def partialsort(array, k):
    return sorted(array)[:k]

def nsort(array, n):
    return sorted(array)[n]

def binarysearch(arr, value):
    idx = bisect_left(arr, value)
    return idx < len(arr) and arr[idx] == value

def lower(v, value):
    return bisect_left(v, value)  # First position for insertion

def upper(v, value):
    return bisect_right(v, value)  # Last position for insertion

def copy(n):
    try: return n.copy()
    except: return n
    
def forall(array, func):
    return list(map(func, array))

def flood(array, val):
    return [val]*len(array)

def floodstr(string, val):
    return f"{val}"*len(string)

def replace(array, old_value, new_value):
    return [new_value if x == old_value else x for x in array]

def removeall(array, value):
    return [x for x in array if x != value]

def unique(array):
    return [key for key, _ in groupby(array)]

def partbyall(array, pred):
    true_part = [x for x in array if pred(x)]
    false_part = [x for x in array if not pred(x)]
    return true_part, false_part

def partbytrue(array, pred):
    true_part = [x for x in array if pred(x)]
    return true_part

def partbyfalse(array, pred):
    false_part = [x for x in array if not pred(x)]
    return false_part

def perms(array):
    return list(permutations(array))

def alogs(array, func):
    results = []
    for i in array:
        results.append(func(i))
    return results