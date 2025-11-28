class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)   
        state = [0] * numCourses 
        
        def dfs(course):
            if state[course] == 1:
                return False     
            if state[course] == 2:
                return True       
            state[course] = 1   
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            state[course] = 2    
            return True
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        
        return True
        