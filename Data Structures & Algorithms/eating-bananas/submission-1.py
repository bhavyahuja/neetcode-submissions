class Solution:
    def eat(self, arr, rate):
        ans=0
        for x in arr:
            ans += (x + rate - 1) // rate
        return ans
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)
        ans=float('inf')
        while l<=r:
            m=(l+r)//2
            if (self.eat(piles,m)<=h):
                r=m-1
                ans=min(ans,m)
            else:
                l=m+1
        return ans