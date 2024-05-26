class Polynomial:

    def __init__(self, coefficients):
        if self!=0:
            self.coefficients=coefficients[::-1]
        else:
            self.coefficients=0
    
    def __add__(self,other):
        lst=[]
        for i in self.coefficients:
            for j in other.coefficients:
                lst.append(i+j)
                break
        return Polynomial(lst)
    
    def __call__(self, param):
        num=0
        for m in range(len(self.coefficients)):
            num+=self[m]*((param)**m)
        return num

    def __repr__(self):
        s=""
        for k in range(len(self.coefficients)):
            if self.coefficients[k]!=0:
                if k!=len(self.coefficients)-1:
                    s+=str(self.coefficients[k])+"x^"+str(len(self.coefficients)-k-1)
                    if self.coefficients[k]
                elif k==len(self.coefficients)-1:
                    s+=str(self.coefficients[k])
                else:
                    s=s[:-1]
        return s

poly1 = Polynomial([3, 7, 0, -9, 2])
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3])
poly3 = poly1 + poly2
print(poly1)




