def move_zeros(nums):
    ct=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[ct] = nums[i]
            ct+=1

    while ct<len(nums):
        nums[ct] = 0        
        ct+=1
    return nums

print(move_zeros([0,1,0,3,13,0]))