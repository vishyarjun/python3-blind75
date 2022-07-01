'''
Approach: Binary Search

Point to note: In a rotated sorted array, when doing binary search, one side will always be sorted and other side will always be incorrectly sorted if 
pivot index k (1 <= k < nums.length)


1. find mid. 
2. if left side is sorted
    - if target is within left limits, binary search on left
    - else binary search on right
3 else (if left side is not sorted, right side is sorted)
    - if target is within right limits, binary search on right
    - else binary search on left


'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[left]>nums[mid]:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
                    
        return -1
