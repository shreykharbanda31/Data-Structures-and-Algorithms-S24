class Vector:
    #(a)
    def __init__(self,d):
        if isinstance(d, list):
            self.coords = d
        else:
            self.coords = [0] * d

    def __len__(self):
        return len(self.coords) 
    
    def __getitem__(self, j):
        return self.coords[j]
    
    def __setitem__(self, j, val):
          self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree") 
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j] 
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'
    
    def __repr__(self):
        return str(self)

    #(b)
    def __sub__(self,other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) 
        for k in range(len(self)):
            result[k]=other[k] - self[k]
        return result
    
    #(c)
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] -= self[i]
        return result

    #(d)
    def __mul__(self, num):
        result = Vector(len(self))
        for l in range(len(self)):
            result[l] = self[l]*num
        return result
    
    #(e)
    def __rmul__(self, num):
        result = Vector(len(self))
        for l in range(len(self)):
            result[l] = num*self[l]
        return result
    
    #(f)
    def __mul__(self, num):
        result = Vector(len(self))
        dprod=0
        if isinstance(num,int):
            for l in range(len(self)):
                result[l] = self[l]*num
            return result
        else:
            if (len(self) != len(num)):
                raise ValueError("dimensions must agree") 
            else:
                for k in range(len(self)):
                    dprod += self[k] * num[k]
            return dprod
    
