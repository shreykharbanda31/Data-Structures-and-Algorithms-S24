from re import L

#a
def create_permutation(n):
    import random
    lst=[]
    while len(lst)!=n:
        jj=random.randint(0,n-1)
        if jj not in lst:
            lst.append(jj)
    return lst
print(create_permutation(6))

#b
def scramble_word(word):
    lst2=create_permutation(len(word))
    print(lst2)
    final=""
    for i in lst2:
        final+=word[i]
    return final
print()
print(scramble_word("pokemon"))

#c
import random
choices=["pokemon","laptop","pencil","opiod"]
word_comp=choices[random.randint(0,len(choices)-1)]
scram_comp=list(scramble_word(word_comp))
print("Unscramble the word: ", " ".join(scram_comp))
s=input("Try #1: ")
if s!=word_comp:
    print("Wrong!")
    j=input("Try #2: ")
    if j!=word_comp:
        print("Wrong!")
        z=input("Try #3: ")
        if z!=word_comp:
            print("Better luck next time!")
        else:
            print("Yay, you got it!")
    else:
        print("Yay, you got it!")
else:
    print("Yay, you got it!")

    