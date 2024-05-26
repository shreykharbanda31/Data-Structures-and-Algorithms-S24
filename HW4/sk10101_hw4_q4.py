def list_min(lst, low, high):
    if low==high:
        return lst[low]
    else:
        return min(list_min(lst, low,high-1), lst[high])


print(list_min([1,2,3,4],0,3))

