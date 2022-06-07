class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            prev = max(nums[i],nums[i]+prev)
            
            ans = max(ans,prev)
            
        return ans
