def remove_all(lst, value):

    last_val=0
    for i in range(len(lst)):
        if lst[i]!=value:
            lst[i], lst[last_val] = lst[last_val], lst[i]
            last_val+=1
    if last_val==0:
        raise ValueError('value not present in list')
    else:
        while last_val<=len(lst)+1:
            lst.pop()
            last_val+=1



