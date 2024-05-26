def permutations(lst, low, high):         
    if low == high:                 
        return [[lst[low]]]         
    p = permutations(lst, low+1, high)         
    result = []          
    x = lst[low]          
    
    for i in p:                 
       
        for j in range(len(i) + 1):                         
            temp = i[:]                         
            temp.insert(j,x)                         
            result.append(temp)         
    return result  
        
print(permutations([1, 2, 3], 0, 2))
