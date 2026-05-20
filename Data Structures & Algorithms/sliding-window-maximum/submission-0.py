class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        pq=[(nums[i], i) for i in range(k)]
        mx=float('-inf')
        heapq.heapify_max(pq)
        ans=[pq[0][0]]
        for i in range(k,len(nums)):
            heapq.heappush_max(pq,(nums[i],i))

            while pq[0][1]<=i-k:
                heapq.heappop_max(pq)
            ans.append(pq[0][0])
        return ans