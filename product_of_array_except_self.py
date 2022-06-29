class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        soln = [1 for i in range(len(nums))]
        left_prod = 1
        for i in range(len(nums)-2,-1,-1):
            soln[i] = soln[i+1]*nums[i+1]
        
        for i in range(len(soln)):
            soln[i] = soln[i]*left_prod
            left_prod*=nums[i]
        
        return soln
