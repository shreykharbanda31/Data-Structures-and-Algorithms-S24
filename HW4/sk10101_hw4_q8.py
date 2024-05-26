def flat_list(nested_lst, low, high):
    if low>high:        
        return []
    else:
        temp = []
        if isinstance(nested_lst[low], list):         
            temp += flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
        else:         
            temp.append(nested_lst[low])     
        temp += flat_list(nested_lst, low + 1, high)    
        return temp
                       
