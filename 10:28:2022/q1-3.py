from ArrayList import ArrayList
from ArrayStack import *

def stack_sum(s):
    if len(s)==0:
        return 0
    else:
        val = s.pop()
        result += val
        result += stack_sum(s)
        s.push(val)
    return result

k = ArrayStack()
k.push(3)
k.push(5)
print(stack_sum(k))

def eval_prefix(exp_str):

    exp_lst = exp_str.split( )
    s  = ArrayStack()
    for i in range(len(exp_lst)-1,-1,-1):
        if exp_lst[i].isdigit():
            s.push(int(exp_lst[i]))
        if exp_lst[i] in "+-/*" and len(s)>=2:
            a1=int(s.pop())
            a2=int(s.pop())
            if exp_lst[i] == '+':
                s.push(a1+a2)
            if exp_lst[i] == '-':
                s.push(a1-a2)
            if exp_lst[i] == '*':
                s.push(a1*a2)
            if exp_lst[i] == '/':
                s.push(a1/a2)
    return s.pop()


print(eval_prefix(" - + * 16 5 * 8 4 20"))

def flatten_list(lst):
    s= ArrayStack()
    for i in range(len(lst)-1,-1,-1):
        if isinstance(lst[i],int):
            s.push(lst[i])
            lst.pop()
        else:
            while len(lst[i])!=0:
                lst[i].extend(lst[i])
            for j in range(len(lst[i]-1,-1,-1)):
                s.push(lst[i][j])
            lst.pop()
    for k in range(len(s)):
        lst.append(s.pop())
    return lst

print(flatten_list([[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]))