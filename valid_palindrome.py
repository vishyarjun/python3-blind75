class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = re.sub('[^A-Za-z0-9]', '', s).lower()
        print(val)
        return val==val[::-1]
