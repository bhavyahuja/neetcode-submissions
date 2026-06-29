class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x] is the min ways to get to x from 0
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                if (i-coin>=0):
                    dp[i]=min(dp[i], dp[i-coin]+1)
        if dp[amount]!=float('inf'):
            return dp[amount]
        else:
            return -1