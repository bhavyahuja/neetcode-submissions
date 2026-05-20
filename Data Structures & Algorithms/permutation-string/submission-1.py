class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt= Counter(s1)
        l=0
        r=len(s1)-1
        k = len(s1)
        for l in range(len(s2)-k+1):
            cnt2 = Counter(s2[l:l+k])
            if(cnt2==cnt):
                return True
            l+=1
            r+=1
        return False
