#(a)

def find_duplicates(lst):
    a = len(lst)
    temp = []
    for i in range(a):
        if (lst[lst[i] % a] >= a): 
            if (lst[lst[i] % a] < 2 * a):
                temp.append(lst[i] % a)  
        lst[lst[i] % a] += a    
    return temp
