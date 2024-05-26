from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    result = []
    
    q = ArrayQueue()
    q.enqueue([])
    s = ArrayStack()

    for k in range(len(lst)):
        s.push(lst[k])

    d = -1
    temp = 0
    is_running = True

    while is_running:
        temp_lst = q.dequeue()

        if d < len(temp_lst):
            if not s.is_empty():
                temp = s.pop()
                d += 1
            else:
                is_running = False
                result.append(temp_lst)


        if is_running:
            for i in range(len(temp_lst)+1):
                new_lst = temp_lst.copy()
                new_lst.insert(i, temp)
                q.enqueue(new_lst)
        
    while not q.is_empty():
        result.append(q.dequeue())
    
    return result




