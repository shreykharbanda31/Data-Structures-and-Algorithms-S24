def split_parity(lst):
    j=len(lst)-1
    i=0
    while i<j:
        if lst[i]%2==0:
            lst[i],lst[j]=lst[j],lst[i]
            j-=1
        else:
            i+=1
    return lst

