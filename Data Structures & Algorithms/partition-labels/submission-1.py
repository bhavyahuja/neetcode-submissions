class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt=Counter(s)
        print(cnt)
        curr=set()
        lenner=0
        ans=[]
        for c in s:
            lenner+=1
            if cnt[c]==1:
                curr.discard(c)
                if not curr:
                    ans.append(lenner)
                    lenner=0
            else:
                curr.add(c)
            cnt[c]-=1
        return ans
            
