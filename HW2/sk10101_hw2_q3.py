def factors(num):
    if int(num**0.5)*int(num**0.5) != int(num):

        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                yield i
        for j in range(int(num**0.5),0,-1):
            if num%j==0:
                yield num//j

    else:

        for i in range(1,int(num**0.5)):
            if num%i==0:
                yield i
        for j in range(int(num**0.5),0,-1):
            if num%j==0:
                yield num//j



