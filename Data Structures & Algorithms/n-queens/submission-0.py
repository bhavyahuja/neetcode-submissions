class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path=[]
        ans=[]
        cols=set()
        dia1=set()
        dia2=set()
        def dfs(row):
            if row==n:
                board=[]
                for c in path:
                    row_str='.'*c+"Q"+"."*(n-c-1)
                    board.append(row_str)
                ans.append(board)
                return
            for col in range(n):
                if col not in cols and row-col not in dia1 and row+col not in dia2:
                    path.append(col)
                    cols.add(col)
                    dia1.add(row-col)
                    dia2.add(row+col)
                    dfs(row+1)
                    path.pop()
                    cols.remove(col)
                    dia1.remove(row-col)
                    dia2.remove(row+col)
        dfs(0)


        return ans
            
