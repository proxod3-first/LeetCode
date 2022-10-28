
# premium task



#class Intervals:
    # def __init__(self, start, end):
    #     self.start = start
    #     self.end = end
    
    
class Solution:
    

    def canAttendMeeting(self, intervals):
        intervals = sorted(intervals, key = lambda x: x.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True