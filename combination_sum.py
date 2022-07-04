class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, tmp, s):
            print(i,tmp,s)
            if s == target:
                res.append(tmp[:])
                return
            if s > target:
                return
            
            for j in range(i, len(candidates)):
                tmp.append(candidates[j])
                backtrack(j, tmp, s + candidates[j])
                tmp.pop()
                
        backtrack(0, [], 0)
        return res
