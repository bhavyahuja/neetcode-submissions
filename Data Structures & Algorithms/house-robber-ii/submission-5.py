class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        def solve(arr):
            n=len(arr)
            if n==1 or n==2:
                return max(arr)
            dp=[0]*(n)
            dp[0],dp[1],dp[2]=arr[0],arr[1], arr[0]+arr[2]
            for i in range(3, n):
                dp[i]=arr[i]+max(dp[i-2],dp[i-3])
            return max(dp)
        
        return max(solve(nums[1:]),solve(nums[:-1]))