class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh_ans = {}
        
        for s in strs:
            sor = ''.join(sorted(s))
            if sor not in hsh_ans:
                hsh_ans[sor] = []
            hsh_ans[sor].append(s)
        
        return [hsh_ans[key] for key in hsh_ans]
