def reverse_list(lst):
    for i in range(len(lst)//2):
        lst[i],lst[len(lst)-i-1]=lst[len(lst)-1-i],lst[i]
    return lst


def reverse_list(lst, low=None, high=None):
    if low==None:
        low=0
    if high==None:
        high=len(lst)-1
    while low<high:
        lst[low],lst[high]=lst[high],lst[low]
        low+=1
        high-=1
    return lst

def shift(lst,k):
    lst=reverse_list(lst,0,len(lst)-1)
    lst=reverse_list(lst,0,k-1)
    lst=reverse_list(lst,k,len(lst)-1)
    return lst
    

