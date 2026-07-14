class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pfx=0
        sfx=0
        n=len(nums)
        ans=float('-inf')
        for i in range(n):
            pfx=nums[i]*(pfx or 1)
            sfx=nums[n-i-1]*(sfx or 1)
            ans=max(ans, max(pfx,sfx))
        return ans
        