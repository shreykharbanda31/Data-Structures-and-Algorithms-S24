def find_missing(lst):

    i=0
    j=len(lst)-1
    
    while i<=j:
        mid=(i+j)//2
        
        if mid==lst[mid]:
            i=mid+1
        else:
            
            
