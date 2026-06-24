class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        visited=set()
        q=deque()

        def addcell(r,c):
            if min(r,c)<0 or r>=R or c>=C or grid[r][c]==0 or (r,c) in visited:
                return
            q.append([r,c])
            visited.add((r,c))
        one=0
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    one=1
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
        
        time=0
        if not q and not one:
            return 0
        while q:
            time+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=2
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c-1)
                addcell(r,c+1)

        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    return -1
        # print(grid)
        return time-1
