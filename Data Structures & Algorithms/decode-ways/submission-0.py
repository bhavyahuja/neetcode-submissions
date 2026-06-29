class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        # state is dp[i] -> how many ways to get to end from i
        dp[n]=1
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                continue
            dp[i]=dp[i+1]
            if i+1<=n-1 and 10<=int(s[i:i+2])<=26:
                dp[i]+=dp[i+2]
        return dp[0]
