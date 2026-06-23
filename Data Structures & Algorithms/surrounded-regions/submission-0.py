class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len(board[0])
        visited=set()
        def dfs(r,c):
            if r<0 or c<0 or r>m-1 or c>n-1:
                return 
            if (r,c) in visited:
                return 
            if board[r][c]!='O':
                return
            board[r][c]='F'
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)

        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='F':
                    board[i][j]='O'
        
        
