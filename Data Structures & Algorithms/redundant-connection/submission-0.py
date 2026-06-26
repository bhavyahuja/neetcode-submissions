class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # print(graph)
        visited=set()
        cycle=set()
        cycleStart=-1
        def dfs(node, prev):
            nonlocal cycleStart
            if node in visited:
                cycleStart=node
                return True
            visited.add(node)
            for n in graph[node]:
                if n==prev:
                    continue
                if dfs(n, node):
                    if cycleStart!=-1:
                        cycle.add(node)
                    if node==cycleStart:
                        cycleStart=-1
                    return True
            return False

        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []

