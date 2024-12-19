def memset(value, size, original_list = [], end_list = []):
    my_list = [value] * size
    return (original_list + my_list + end_list)


def indset(l, start=0):
    return range(start, len(l))

def allint(vals):
    return map(int, vals)

def clamp(val, minimum, maximum):
    return max(min(val, maximum), minimum)

def flatten(xss):
    return [x for xs in xss for x in xs]
