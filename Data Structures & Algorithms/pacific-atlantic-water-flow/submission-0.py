class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights), len(heights[0])
        def dfs(r,c, visited):
            if r<0 or r>m-1 or c<0 or c>n-1:
                return
            if (r,c) in visited:
                return
            visited.add((r,c))
            if r+1<=m-1 and heights[r+1][c]>=heights[r][c]:
                dfs(r+1,c,visited)
            if r-1>=0 and heights[r-1][c]>=heights[r][c]:
                dfs(r-1,c,visited)
            if c+1<=n-1 and heights[r][c+1]>=heights[r][c]:
                dfs(r,c+1,visited)
            if c-1>=0 and heights[r][c-1]>=heights[r][c]:
                dfs(r,c-1,visited)
        
        visitedp=set()
        visiteda=set()
        for i in range(m):
            dfs(i,0,visitedp)
            dfs(i,n-1,visiteda)
        for i in range(n):
            dfs(0,i,visitedp)
            dfs(m-1,i,visiteda)
        
        common=visitedp & visiteda
        return list(common)