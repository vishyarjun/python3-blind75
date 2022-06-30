'''
Brute Force: calculate area height against every other height O(n^2)
Optimal approach: start from maximum width, calculate area and reduce the width based on maximum value of left and right
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 points one from left and one from right
        # aim is to 
        left,right = 0,len(height)-1
        mxArea = 0
        while left<right:
            # area is (distance between 2 heights) x (miminum among 2 heights)
            mxArea = max(mxArea, min(height[left],height[right])*(right-left))
            
            #keep moving either left or right till becomes a bigger height.
            if height[left]>height[right]: 
                right-=1
            else: 
                left+=1
        return mxArea
        # Time Complexity: O(N), Space Complexity: O(1)
