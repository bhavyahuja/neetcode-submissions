class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 or n==2:
            return max(nums)
        dp=[0]*(n+1)
        dp[0],dp[1],dp[2]=nums[0],nums[1], nums[0]+nums[2]
        for i in range(3, n):
            dp[i]=nums[i]+max(dp[i-2],dp[i-3])
        return max(dp)