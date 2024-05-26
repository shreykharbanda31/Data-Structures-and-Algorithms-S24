#(a)
def sum_square(n):
    final=0
    for i in range(1,n):
        final+=i**2
    return final


n=int(input("Enter a positive integer: "))

#(b)
x=sum([i**2 for i in range(1,n)])

#(c)
def sum_oddsquares(n):
    final=0
    for i in range(1,n,2):
        final+=i**2
    return final

#(d)
y=sum([i**2 for i in range(1,n,2)])

