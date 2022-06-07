class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],x[1]))
        curr = intervals[0]
        ans = 0
        for i in range(1,len(intervals)):
            if intervals[i][0]<curr[1]<=intervals[i][1] or curr[0] <= intervals[i][0] < curr[1]:
                if intervals[i][1]<curr[1]:
                    curr = intervals[i]
                ans+=1
            else:
                curr = intervals[i]
        return ans
