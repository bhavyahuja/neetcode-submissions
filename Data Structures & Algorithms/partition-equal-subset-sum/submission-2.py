class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        # print(summ)
        if total % 2 != 0:
            return False
        nums.sort()
        n=len(nums)
        target=total//2
        # dp=[[False]*(target+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0]=True
        # for i in range(1,n+1):
        #     for j in range(1,target+1):
        #         if nums[i-1]<=j:
        #             dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
        #         else:
        #             dp[i][j]=dp[i-1][j]
        # return dp[n][target]

        dp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j]=dp[j] or dp[j-num]
        return dp[target]
