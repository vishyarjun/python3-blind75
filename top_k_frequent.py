class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            hsh[n] = 1 + hsh.get(n, 0)
        for n, c in hsh.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
