class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        # dp=[[float('-inf')]*n for _ in range(n)]
        # mnsum=mxsum=nums[0]
        # if n==1:
        #     return nums[0]
        # mx=nums[0]
        # for x in nums[1:]:
        #     mxsumm=mxsum
        #     mxsum=max(x,mxsum*x,mnsum*x)
        #     mnsum=min(x,mxsumm*x,mnsum*x)
        #     mx=max(mx,mxsum)
        # return mx

        pre=0
        suff=0
        res=nums[0]
        for i in range(n):
            pre=nums[i]*(pre or 1)
            suff=nums[n-i-1]*(suff or 1)
            res=max(res,max(pre,suff))
        return res
