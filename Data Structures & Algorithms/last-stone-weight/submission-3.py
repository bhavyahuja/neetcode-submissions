class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones)>1:
            big1 = -heapq.heappop(stones)
            big2 = -heapq.heappop(stones)
            ans=abs(big1-big2)
            if ans>0:
                heapq.heappush(stones, -ans)
        return -stones[0] if stones else 0