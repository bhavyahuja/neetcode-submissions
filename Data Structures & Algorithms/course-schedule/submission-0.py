class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited=set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for p in graph[course]:
                if not dfs(p):
                    return False
            path.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            path=set()
            if not dfs(course):
                return False
        return True
