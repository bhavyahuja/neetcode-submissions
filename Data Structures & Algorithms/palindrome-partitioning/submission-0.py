class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path=[]
        ans=[]
        def dfs(start):
            if start==len(s):
                ans.append(path.copy())
                return
            for end in range(start, len(s)):
                if s[start:end+1]==s[start:end+1][::-1]:
                    path.append(s[start:end+1])
                    dfs(end+1)
                    path.pop()

        dfs(0)
        return ans
                