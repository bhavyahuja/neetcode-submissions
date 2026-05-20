from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt=defaultdict(int)
        l=0
        ans=0
        maxFreq=0
        for r in range(len(s)):
            cnt[s[r]]+=1
            maxFreq = max(maxFreq, cnt[s[r]])
            while k<(r-l+1)-maxFreq:
                cnt[s[l]]-=1
                l+=1
            ans=max(ans, r-l+1)
        return ans