def maxsum(nums,k):
    i=0
    max_sum=0
    while i<len(nums)//k:
        max_sum+=nums[i]
        i+=1
    
    sum=max_sum
    while i<len(nums):
        sum+=nums[i] - nums[i-len(nums)//k]
        max_sum=max(sum, max_sum)
        i+=1
    return max_sum



