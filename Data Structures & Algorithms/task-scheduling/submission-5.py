class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt=Counter(tasks)
        # print(cnt)
        maxFreq = max(cnt.values())
        numMax=0
        for freq in cnt.values():
            if freq==maxFreq:
                numMax+=1

        ans=(maxFreq-1)*(n+1)+numMax
        return max(ans,len(tasks))