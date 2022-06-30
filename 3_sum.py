class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums 
        temp = set()
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1

            r = len(nums) - 1

            while l<r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    temp.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r-=1 #this optimization will reduce the number of iterations. if we incremenrt l, then we wont get 0 unless the nums[l] is the same value as before. however if nums[l] is the same, we need not add it to res. hence while we do l+1, we can also do r-1
        return list(temp)
