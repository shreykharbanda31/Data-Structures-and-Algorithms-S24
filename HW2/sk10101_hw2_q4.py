def e_approx(n):
    mult=1
    sum=1
    for i in range(1,n+1):
        mult*=i
        sum+=1/(mult)
    return sum

