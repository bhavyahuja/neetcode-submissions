class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntT=Counter(t)
        cntS=Counter()
        l=0
        ans=''
        minLen = float('inf')
        for r in range(len(s)):
            cntS[s[r]]+=1
            while (cntT<=cntS):
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    ans = s[l:r+1]
                l+=1
                cntS[s[l-1]]-=1
        return ans
