#(a)
def shift(lst, k):
    for i in range(k):
        lst.append(lst.pop(0))
    return lst

#(b)
def shift(lst, k, direction='left'):
    if direction=='left':
        for i in range(k):
            lst.append(lst.pop(0))
    else:
        for i in range(k):
            lst.insert(0,lst.pop())
    return lst
