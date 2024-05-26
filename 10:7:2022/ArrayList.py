import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self,iterable_collection=None):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0
        if isinstance(iterable_collection, str):
            for i in iterable_collection:
                self.append(i)
        if isinstance(iterable_collection, int):
            for i in range(iterable_collection):
                self.append(i)


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if -self.n<=ind<=-1:
            return self.data_arr[len(self)+ind]
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if -self.n<=ind<=-1:
            self.data_arr[len(self)+ind]=val
        else:
            self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        str1=""
        str1+="["
        for i in range(self.n-1):
            str1+=str(self[i])+", "
        str1+=str(self[self.n-1])
        return str1+"]"

    def __add__(self,other):
        d=ArrayList()
        d.extend(self)
        d.extend(other)
        return d

    def __iadd__(self,other):
        self.extend(other)
        return self

    def __mul__(self,val):
        d=ArrayList()
        for j in range(val):
            d.extend(self)
        return d

    def __rmul__(self,val):
        return self*val

    def remove(self,val):
        i=0; ind=0; flag=True
        while i<self.n and flag:
            if self[i]==val:
                flag=False
                ind=i
            i+=1       
        
        while ind<self.n-1:
            self[ind]=self[ind+1]
            ind+=1
        
        if ind<self.n:
            self[ind]=None
            self.n-=1

    def removeAll(self,val):

        last_val=0
        for i in range(len(self)):
            if self[i]!= val:
                self[i], self[last_val] = self[last_val], self[i]
                last_val+=1

        while self[i] == val:
            self[i] = None
            i-=1
            self.n -=1


def main():
        
        lst=ArrayList()
        lst.append(5)
        lst.append(6)
        lst.append(10)
        print(lst)
        lst[-2]=90
        lst2=ArrayList()
        lst2.append(1)
        lst2.append(2)
        print(lst)
        lst3=ArrayList(10)
        lst3.remove(9)
        print(lst3)


main()