class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        out = ""
        for s in strs:
            l = str(len(s))
            out+=(str(len(l))+l+s)
        print(out)
        return out

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        out = []
        i=0
        while i < len(str):
            l1 = int(str[i])
            l2 = int(str[i+1:i+1+l1])
            st = i+1+l1
            end = st+l2
            out.append(str[st:end])
            i = end
        return out
        # write your code here
