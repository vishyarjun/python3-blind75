class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx_len = 0
        curr_max = 0
        hsh_freq = {}
        left, right = 0,0
        while right<len(s):
            char = s[right]
            hsh_freq[char] = hsh_freq.get(char,0)+1
            curr_max = max(curr_max,hsh_freq[char])
            if (right-left+1)-curr_max<=k:
                mx_len = max(right-left+1,mx_len)
            else:
                hsh_freq[s[left]]-=1
                left+=1
            right+=1
        return mx_len
            
