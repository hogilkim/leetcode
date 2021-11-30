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