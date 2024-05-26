def reverse_vowels(input_str):

    list_str = list(input_str)
    i=0
    j=len(list_str)-1

    while i<=j:
        if list_str[j] not in "aeiou":
            j-=1
        elif list_str[i] not in "aeiou":
            i+=1
        else:
            list_str[i],list_str[j]=list_str[j],list_str[i]
            i+=1
            j-=1

    return "".join(list_str)
            
print(reverse_vowels("shreya"))


            
