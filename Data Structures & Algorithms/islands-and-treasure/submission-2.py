class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return
            if grid[r][c]==-1:
                return
            # if grid[r][c]==0:
            #     return
            dir=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in dir:
                nr,nc=r+dr,c+dc
                if 0<=nr<=m-1 and 0<=nc<=n-1 and grid[nr][nc]>grid[r][c]:
                    grid[nr][nc]=grid[r][c]+1
                    dfs(nr,nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    dfs(i,j)
        

                
            