class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R,C=len(matrix),len(matrix[0])
        dp={}
        def dfs(r,c,prevVal):
            if r>R-1 or c>C-1 or r<0 or c<0 or matrix[r][c]<=prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1
            res=max(res,1+ dfs(r+1,c,matrix[r][c]))
            res=max(res,1+ dfs(r,c+1,matrix[r][c]))
            res=max(res,1+ dfs(r-1,c,matrix[r][c]))
            res=max(res,1+ dfs(r,c-1,matrix[r][c]))
            dp[(r,c)]=res
            return res

        for r in range(R):
            for c in range(C):
                dfs(r, c, -1)
        return max(dp.values())