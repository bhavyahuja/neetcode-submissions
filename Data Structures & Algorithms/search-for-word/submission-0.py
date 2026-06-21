class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=[]
        visited=set()
        m,n=len(board),len(board[0])
        def dfs(row, col,i):
            if (
                row < 0 or row >= m or
                col < 0 or col >= n or
                (row, col) in visited or
                board[row][col] != word[i]
            ):
                return False
            if i==len(word)-1:
                return True
            
            visited.add((row,col))
            
            found = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
            )

            visited.remove((row, col))

            return found

        for cell_row in range(len(board)):
            for cell_col in range(len(board[0])):
                if dfs(cell_row, cell_col, 0):
                    return True
        return False