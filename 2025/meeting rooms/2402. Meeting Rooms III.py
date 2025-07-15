class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        room_usage = [0] * n
        meetings.sort()

        free_rooms = list(range(n))
        heapq.heapify(free_rooms)  # room_id 当前空闲的会议室编号，最小堆
        busy_rooms = [] # (end_time, room_id) 当前使用中的会议室，按照结束时间最早的在前

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room_id = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_id) #？
            
            duration = end -  start

            if free_rooms:
                room_id = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room_id))
            else:
                soonest_end_time, room_id = heapq.heappop(busy_rooms)
                new_end_time = soonest_end_time +duration
                heapq.heappush(busy_rooms, (new_end_time, room_id))
            
            room_usage[room_id] += 1
        max_usage = max(room_usage)
        for i, count in enumerate(room_usage):
            if count == max_usage:
                return i
