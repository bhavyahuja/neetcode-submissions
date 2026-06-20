class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        candidates.sort()
        def dfs(i, remaining):
            
            if remaining==0:
                ans.append(path.copy())
                return
            if remaining<0:
                return
            for j in range(i, len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(j+1, remaining-candidates[j])
                path.pop()
        dfs(0, target)
        return ans