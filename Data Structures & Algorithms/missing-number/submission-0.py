class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        summ=int(((n)*(n+1))/2)
        sumact=0
        for i in nums:
            sumact+=i
        ans=(summ-sumact)
        return ans