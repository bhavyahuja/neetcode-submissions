class Solution:
    def jump(self, nums: List[int]) -> int:
        # BAD DP O(n^2)
        # need=len(nums)-1
        # arr=[float('inf')]*len(nums)
        # arr[need]=0
        # print(arr)
        # for i in range(len(nums)-2, -1,-1):
        #     if nums[i]+i>=need:
        #         arr[i]=1
        #     else:
        #         arr[i]=min(arr[i:i+nums[i]+1])+1
        # return arr[0]

        # BFS
        left,right=0,0
        jumps=0
        while right < len(nums)-1:
            farthest=0
            for i in range(left, right+1):
                farthest=max(farthest, i+nums[i])
            left=right+1
            right=farthest
            jumps+=1
        return jumps




