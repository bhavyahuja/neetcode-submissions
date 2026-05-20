class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans=[]
        # pq=[(nums[i], i) for i in range(k)]
        # mx=float('-inf')
        # heapq.heapify_max(pq)
        # ans=[pq[0][0]]
        # for i in range(k,len(nums)):
        #     heapq.heappush_max(pq,(nums[i],i))

        #     while pq[0][1]<=i-k:
        #         heapq.heappop_max(pq)
        #     ans.append(pq[0][0])
        # return ans
        dq=deque()
        ans=[]
        l=r=0
        while (r < len(nums)):
            while dq and nums[dq[-1]]<nums[r]:
                dq.pop()

            dq.append(r)
            if l>dq[0]:
                dq.popleft()
            if(r+1)>=k:
                ans.append(nums[dq[0]])
                l+=1
            r+=1
        return ans