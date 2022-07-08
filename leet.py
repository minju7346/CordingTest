n = len(nums)
l, r = 0,0
while r<n:
    if nums[r]==0:r+=1
    else:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r+=1