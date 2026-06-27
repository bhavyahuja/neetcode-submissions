class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=len(nums)-2
        n=1
        if len(nums)==1:
            return True
        while i>=0:
            if nums[i]>=n:
                if i==0:
                    return True
                i-=1
                n=1
            else:
                i-=1
                n+=1
        return False
