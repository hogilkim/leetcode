# solve again
# second attempt - Jan 14, 2022
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        
        start = sorted(start)
        end = sorted(end)
        
        room_counter = 0
        max_counter = 0
        start_ptr, end_ptr = 0, 0
        while start_ptr < len(start):
            if start[start_ptr] < end[end_ptr]:
                room_counter += 1
                start_ptr += 1
            else:
                room_counter -= 1
                end_ptr += 1
            max_counter = max(max_counter, room_counter)
            
        return max_counter

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        start = sorted(start)
        end = sorted(end)
        
        room_counter = 0
        max_room = 0
        start_pointer = 0 
        end_pointer = 0
        
        while start_pointer < len(start):
            if start[start_pointer] < end[end_pointer]:
                room_counter += 1
                start_pointer += 1
            else:
                room_counter -= 1
                end_pointer += 1
            max_room = max(max_room, room_counter)
        
        return max_room