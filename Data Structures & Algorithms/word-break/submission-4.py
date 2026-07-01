class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(n-1,-1,-1):
            for w in wordDict:
                if s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]==True:
                    break
        return dp[0]