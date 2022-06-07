class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        
        for i in range(1,len(intervals)):
            last = merged_intervals[-1]
            if intervals[i][0]<=last[1]<=intervals[i][1] or last[0]<=intervals[i][0]<=last[1]:
                merged_intervals[-1] = [min(intervals[i][0], last[0]),max(intervals[i][1], last[1])]
            elif intervals[i][0]>=last[0] and intervals[i][1]<=last[1]:
                pass
            else:
                merged_intervals.append(intervals[i])
        return merged_intervals
