def can_construct(word , letters):
    l_word=list(word)
    l_letters=list(letters)
    track=True
    for n in l_word:
        if n not in l_letters:
            track=False
            break
        else:
            l_letters.remove(n)
    return track

print(can_construct("shey", "yshe"))



        
    

    
