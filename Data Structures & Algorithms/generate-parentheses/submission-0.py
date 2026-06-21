class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path=[]
        ans=[]
        def dfs(open_c, close_c):
            if len(path)==2*n:
                ans.append("".join(path))
                return
            if open_c<n:
                path.append('(')
                dfs(open_c+1, close_c)
                path.pop()
            if close_c<open_c:   
                path.append(')')
                dfs(open_c, close_c+1)
                path.pop()
        dfs(0,0)
        return ans