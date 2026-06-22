class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close=[]
        for n in points:
            dist=n[0]*n[0]+n[1]*n[1]
            heapq.heappush_max(close,(dist, n))
            if len(close)>k:
                heapq.heappop_max(close)
        ans=[]
        for i in range(k):
            ans.append((heapq.heappop_max(close)[1]))
        return ans