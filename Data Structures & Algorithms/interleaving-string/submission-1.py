class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s3)
        n1,n2=len(s1),len(s2)
        dp=[[False]*(n1+1) for _ in range(n2+1)]
        if n1+n2!=n:
            return False
        dp[n2][n1]=True
        for i in range(n2,-1,-1):
            for j in range(n1,-1,-1):
                if i<n2 and dp[i+1][j] and s2[i]==s3[i+j]:
                    dp[i][j]=True
                if j<n1 and dp[i][j+1] and s1[j]==s3[i+j]:
                    dp[i][j]=True
        return dp[0][0]
            