'''
#1
theta(n)

#2
theta(log(n))

#3
theta(n^2): slicing takes n -1, n-2, n-3 for n-1 calls and hence n^2
'''
def sum_to (n):
    if n==0:
        return 0
    else:
        return n + sum_to(n-1)

def product_evens(n):
    if n==2:
        return 2
    else:
        return n * product_evens(n-2)

#Q3 theta(n^2): slicing takes n -1, n-2, n-3 for n-1 calls and hence n^2

def find_max(lst, low, high):
    if low == high:
        return lst[low]
    else:
        return max(find_max(lst, low+1, high), lst[high])


def is_palindrome (str, low, high):

        if low == high :
            if str[low]==str[high]:
                return True 
            else:
                return False
        else:
            return is_palindrome(str, low+1, high-1) and str[low]==str[high]
            

print(is_palindrome("racecar", 1, 4))


def binary_search(lst, low, high, val):
    
    if low>high:
        return -1
    mid = (low+high)//2
    if lst[mid]==val:
        return mid
    elif lst[mid]> val:
        return binary_search(lst, low, mid -1, val)
    else:
        return binary_search(lst,mid+1, high, val)


def vc_count(word, low, high):
    v=0
    c=0
    if low == high:
        if word[low] in "aeiou" or word[low] in "AEIOU":
            return (1,0)
        else:
            return (0,1)
    else:
        v,c = vc_count(word, low+1, high)
        if word[low] in "aeiou" or word[low] in "AEIOU":
            v+=1
        else:
            c+=1
        return (v,c)

print(vc_count("NYUTandonEngineering", 0, len("NYUTandonEngineering")-1))
