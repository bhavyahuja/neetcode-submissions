class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sm=prices[0]
        ans=0
        for p in prices[1:]:
            if p>sm:
                curr=p-sm
                ans=max(curr,ans)
            else:
                sm=p
            
        return ans