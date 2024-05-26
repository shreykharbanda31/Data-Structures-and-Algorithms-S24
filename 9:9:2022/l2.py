class Complex:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __add__(self, other):
        x=Complex(self.a+other.a,self.b+other.b)
        return x
    def __sub__(self, other):
        y=Complex(self.a-other.a,self.b-other.b)
        return y
    def __mul__(self, other):
        z=Complex((self.a*other.a)-(self.b*other.b),(self.a*other.b)+(self.b*other.a))
        return z
    def __iadd__(self, other):
        self.a=self.a+other.a
        self.b=self.b+other.b
        return self
    def __repr__(self):
        return str(self.a)+" + "+str(self.b)+"i"

foo=Complex(5,2)
gg=Complex(3,3)
print(foo+gg)
print(foo-gg)
print(foo*gg)
print(foo)
print(gg)
foo+=gg
print(foo)
print(gg)





        
