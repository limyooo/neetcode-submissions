"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        room = 0
        max_room = 0
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        i,j = 0,0
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                room += 1
                max_room = max(room,max_room)
                i +=1
            elif start[i] >= end[j]:
                room -= 1
                j += 1
        return max_room

