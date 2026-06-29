class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        # dp=[[float('-inf')]*n for _ in range(n)]
        mnsum=mxsum=nums[0]
        if n==1:
            return nums[0]
        mx=float('-inf')
        for x in nums[1:]:
            mxsumm=mxsum
            mxsum=max(x,mxsum*x,mnsum*x)
            mnsum=min(x,mxsumm*x,mnsum*x)
            mx=max(mx,mxsum)
        return mx
