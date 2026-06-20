class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        used=[False]*len(nums)
        def dfs():
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                dfs()
                path.pop()
                used[i]=False

        dfs()
        return ans
