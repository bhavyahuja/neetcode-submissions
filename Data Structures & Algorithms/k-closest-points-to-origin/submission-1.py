class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close=[]
        for n in points:
            dist=n[0]*n[0]+n[1]*n[1]
            heapq.heappush(close,(dist, n))
        ans=[]
        for i in range(k):
            ans.append((heapq.heappop(close)[1]))
        return ans