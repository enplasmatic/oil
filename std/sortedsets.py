def ssunion(v1, v2):
    return sorted(set(v1).union(v2))

def ssintersection(v1, v2):
    return sorted(set(v1).intersection(v2))

def ssdiff(v1, v2):
    return sorted(set(v1).difference(v2))

def sssymmetricdiff(v1, v2):
    result = sorted(set(v1).symmetric_difference(v2))
    return result

def ss(v):
    return sorted(set(v))

