class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        mp = {'}':'{',']':'[',')':'('}
        stk = []
        for char in s:
            if char not in mp.keys():
                stk.append(char)
            else:
                if len(stk)==0 or stk[-1]!=mp[char]:
                    return False
                else:
                    stk.pop()
        
        return True if len(stk)==0 else False
                
        
