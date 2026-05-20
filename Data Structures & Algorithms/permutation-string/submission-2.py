class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt= Counter(s1)
        cnt2=Counter(s2[:len(s1)])
        l=0
        r=len(s1)-1
        k = len(s1)
        if(cnt==cnt2):
            return True
        for r in range(k,len(s2)):
            cnt2[s2[r]]+=1
            cnt2[s2[l]]-=1
            l+=1
            r+=1
            if cnt == cnt2:
                return True
        return False
