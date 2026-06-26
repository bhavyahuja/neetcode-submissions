class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        prev=0
        visited=set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for n in graph[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True

        if not dfs(0,-1):
            return False

        return len(visited) == n