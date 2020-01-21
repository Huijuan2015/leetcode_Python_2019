class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #has interval: a new room needed
        # Whenever you want to start a meeting, 
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).  
 # After you finish the meeting, the room becomes available again ( available += 1 ).
    #[0, 5, 15] 要开始meeting， new room如果没有available； [10, 20, 30] 有meeting结束释放room
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        
        starts.sort()
        ends.sort()
        s, e = 0, 0
        rooms, available = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                # need a room
                if available == 0:
                    rooms += 1
                else:
                    available -= 1
                s += 1
            else: # release a room
                available += 1
                e += 1
        return rooms