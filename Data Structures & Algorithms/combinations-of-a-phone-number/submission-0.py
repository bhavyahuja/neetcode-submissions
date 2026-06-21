class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans=[]
        path=[]
        if not digits:
            return []
        def dfs(i):
            if len(path)==len(digits):
                ans.append("".join(path))
                return

            for c in mp[digits[i]]:
                path.append(c)
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans