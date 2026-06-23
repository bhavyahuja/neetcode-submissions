class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        m,n=len(grid),len(grid[0])
        sum=0
        def dfs(r,c):
            nonlocal sum
            if r<0 or c<0 or r>=m or c>=n:
                return 0
            if (r,c) in visited:
                return 0
            if grid[r][c]==0:
                return 0
            visited.add((r,c))
            return (1+
            dfs(r+1,c)+
            dfs(r,c+1)+
            dfs(r-1,c)+
            dfs(r,c-1))
        ans=0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]==1:
                    sum=0
                    ans=max(ans, dfs(i,j))
        return ans
            
            