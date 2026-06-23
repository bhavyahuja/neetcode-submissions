class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        m,n=len(grid),len(grid[0])
        visited=set()
        def dfs(r,c):
            if r>=m or r<0 or c>=n or c<0:
                return
            if grid[r][c]=='0':
                return
            if (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    ans+=1
                    dfs(i,j)
        return ans