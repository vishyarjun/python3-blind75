'''
1: 0
0: 1



'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        visited = set()
        visiting = set()
        for pre in prerequisites:
            if pre[0] in courses:
                courses[pre[0]].append(pre[1])
            else:
                courses[pre[0]] = [pre[1]]      
        def helper(i):
            if i in visiting:
                return False
            if i in visited or i not in courses:
                return True
            visiting.add(i) # 0
            for item in courses.get(i):
                if not helper(item):
                    return False
            visited.add(i)
            visiting.remove(i)
            return True
            
    
        for i in range(numCourses):
            if i in courses and i not in visited:
                if not helper(i):
                    return False
        return True
                
        
        
