class Solution:    
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        hsh_t = Counter(t)
        hsh_s = {}
        l = 0
        cnt = 0
        ans = ""
        for r in range(len(s)):
            c = s[r]
            if c in hsh_t:
                hsh_s[c] = hsh_s.get(c,0) + 1
                if hsh_s[c]==hsh_t[c]:
                    cnt+=1
                    while cnt == len(hsh_t):
                        cur = s[l:r+1]
                        if len(ans)==0 or len(cur) < len(ans):
                            ans = cur
                        
                        if s[l] in hsh_t:
                            hsh_s[s[l]]-=1
                            if hsh_s[s[l]]<hsh_t[s[l]]:
                                cnt-=1
                        l+=1
        return ans
