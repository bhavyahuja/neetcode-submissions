class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights), len(heights[0])
        def dfs(r,c, visited):
            if r<0 or r>m-1 or c<0 or c>n-1:
                return
            if (r,c) in visited:
                return
            visited.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        
        visitedp=set()
        visiteda=set()
        for i in range(m):
            dfs(i,0,visitedp)
            dfs(i,n-1,visiteda)
        for i in range(n):
            dfs(0,i,visitedp)
            dfs(m-1,i,visiteda)
        
        common=visitedp & visiteda
        return [[r,c] for r,c in common]