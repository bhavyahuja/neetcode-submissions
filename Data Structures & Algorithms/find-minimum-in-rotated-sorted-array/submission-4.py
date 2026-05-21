class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        small=nums[0]
        if len(nums)==2:
            return min(nums[0],nums[1])
        while (l<r):
            m=(l+r)//2
            if(nums[m]>nums[r]):
                l=m+1
            else:
                r=m
        return nums[l]