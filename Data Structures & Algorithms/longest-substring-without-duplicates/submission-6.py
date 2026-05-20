class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ans=0
        # for i in range(len(s)):
        #     if i>=len(s):
        #         break
        #     ch=s[i]
        #     j=i
        #     seen=set()
        #     seen.add(ch)
        #     while(j+1<len(s) and s[j+1] not in seen):
        #         seen.add(s[j+1])
        #         j+=1
        #     ans=max(len(seen),ans)
        #     i=j
        # return ans
        ans=0
        l=0
        seen=set()
        ans=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ans=max(ans, r-l+1)
        return ans
