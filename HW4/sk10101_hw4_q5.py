#(a)

def count_lowercase(s, low, high):
    if low == high:
        if 97<=ord(s[low])<(97+26):
            return 1
        else:
            return 0
    else:
        m = count_lowercase(s, low+1, high)
        if 97<=ord(s[low])<(97+26):
            m +=1
        return m

#(b)

def is_number_of_lowercase_even(s, low, high):     
    if low > high:         
        return True     
    else:         
        if 97<=ord(s[low])<(97+26):             
            return not is_number_of_lowercase_even(s, low + 1, high)         
        else:             
            return is_number_of_lowercase_even(s, low + 1, high)   
