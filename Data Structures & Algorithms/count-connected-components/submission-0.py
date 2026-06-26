class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans=0
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in graph[node]:
                dfs(n)
        
        for node in range(n):
            if node not in visited:
                ans+=1
                dfs(node)
        return ans