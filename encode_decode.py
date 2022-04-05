'''
URL: https://leetcode.com/problems/encode-and-decode-strings/

Introduction: Solution to the famous encode and decode leetcode problem


Algorithm:

consider encoding the word ALPHANUMERICVALUE

total length is 17, we are going to encode as follows

length of the length + length of the word + word

length(ALPHANUMERICVALUE) = 17
length(17) = 1

encoded output 117ALPHANUMERICVALUE

perform this for every string. reverse perform this during decoding.

'''




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
