import heapq
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        NO_OF_MEETINGS = len(intervals)
        if NO_OF_MEETINGS<=1:
            return NO_OF_MEETINGS
        NO_OF_ROOMS = 0
        mn_heap = []
        intervals.sort(key = lambda x:x.start)

        for i in range(NO_OF_MEETINGS):
            while len(mn_heap)>0 and intervals[i].start>=mn_heap[0]:
                heapq.heappop(mn_heap)
            heapq.heappush(mn_heap,intervals[i].end)
            NO_OF_ROOMS = max(NO_OF_ROOMS,len(mn_heap))
        return NO_OF_ROOMS
'''

'''




