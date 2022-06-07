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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        intervals.sort(key = lambda x:x.start)
        prev = intervals[0]
        for i in range(1,len(intervals)):
            curr = intervals[i]
            if prev.end > curr.start:
                return False
            prev = curr
        return True

