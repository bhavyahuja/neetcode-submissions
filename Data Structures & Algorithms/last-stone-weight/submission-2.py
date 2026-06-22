class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ans=0
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        print(stones)
        while stones and len(stones)>=2:
            big1=-stones[0]
            heapq.heappop(stones)
            big2=-stones[0]
            heapq.heappop(stones)
            ans=abs(big1-big2)
            if ans>0:
                heapq.heappush(stones, -ans)
        if len(stones)==1:
            return -stones[0]
        return ans