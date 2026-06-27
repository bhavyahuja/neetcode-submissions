class Solution:
    def jump(self, nums: List[int]) -> int:
        need=len(nums)-1
        arr=[float('inf')]*len(nums)
        arr[need]=0
        print(arr)
        for i in range(len(nums)-2, -1,-1):
            if nums[i]+i>=need:
                arr[i]=1
            else:
                arr[i]=min(arr[i:i+nums[i]+1])+1
        return arr[0]