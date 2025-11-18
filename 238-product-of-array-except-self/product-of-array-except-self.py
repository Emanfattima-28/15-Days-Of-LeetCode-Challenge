class Solution(object):
    def productExceptSelf(self, nums):
        size=len(nums)
        answer=[1]*size
        prefix = 1
        for i in range(size):
            answer[i]=prefix
            prefix*=nums[i]

        suffix = 1
        for i in range(size-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
        return answer

        
        