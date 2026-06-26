class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        order=[]

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
            order.append(course)
            return True
        
        for course in range(numCourses):
            path=set()
            if not dfs(course):
                return []
        return order
