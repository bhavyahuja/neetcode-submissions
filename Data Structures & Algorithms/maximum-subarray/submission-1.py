class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        ans=nums[0]
        for x in nums:
            sum=max(x, sum+x)
            ans=max(sum, ans)
        return ans