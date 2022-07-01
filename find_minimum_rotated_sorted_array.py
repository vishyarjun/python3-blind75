class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]
        left, right = 0,len(nums)-1
        while left<=right:
            if left+1==right:
                return min(nums[left],nums[right])
            mid = (left+right)//2
            # if the left side is sorted, store the smallest value (left index)
            if nums[left]<=nums[mid]:
                left=mid
            else:
                right = mid
