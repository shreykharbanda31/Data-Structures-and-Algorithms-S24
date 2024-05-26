def findChange(lst01):
    i=0
    j=len(lst01)-1
    while i<=j:
        if lst01[0]==1:
            return 0
        mid=(i+j)//2
        if lst01[mid]==1 and lst01[mid-1]==0:
                return mid
        elif lst01[mid]==0:
            i=mid+1
        else:
            j=mid-1
    return None




        
