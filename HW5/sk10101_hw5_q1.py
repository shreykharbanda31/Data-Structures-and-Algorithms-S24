from ArrayStack import *

variables = {}

flag = True
while flag:
    useri = input("--> ")
    
    if useri == "done()":
        flag = False
    else:
        exp = ''
        if len(useri) == 1:
            if useri in variables:
                print(variables[useri])
            else:
                print(useri)
        
        else:

            if useri[2] == '=':
                sub = useri[4:]
            else:
                sub = useri
                
            for i in sub:
                if i in variables:
                    exp += str(variables[i])
                else:
                    exp += i

            exp_lst = exp.split()
            s  = ArrayStack()
            for i in range(len(exp_lst)):
                if exp_lst[i].isdigit():
                    s.push(int(exp_lst[i]))
                if exp_lst[i] in "+-/*" and len(s)>=2:
                    a2=int(s.pop())
                    a1=int(s.pop())
                    if exp_lst[i] == '+':
                        s.push(a1+a2)
                    if exp_lst[i] == '-':
                        s.push(a1-a2)
                    if exp_lst[i] == '*':
                        s.push(a1*a2)
                    if exp_lst[i] == '/':
                        s.push(a1/a2)

            if useri[2] == '=':
                variables[useri[0]] = s.pop()
                print(useri[0])
            else:
                print(s.pop())
                

            
            
    