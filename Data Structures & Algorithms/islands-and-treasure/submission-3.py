class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C=len(grid),len(grid[0])
        visited=set()
        q=deque()

        def addcell(r,c):
            if min(r,c)<0 or r>=R or c>=C or (r,c) in visited or grid[r][c]==-1:
                return
            visited.add((r,c))
            q.append([r,c])
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))

        dist =0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                addcell(r+1, c)
                addcell(r,c+1)
                addcell(r,c-1)
                addcell(r-1,c)
            dist+=1