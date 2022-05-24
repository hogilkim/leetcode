class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # id, start_time
        call_stack = []
        curr_time = 0
        times = [0]*n
        
        for log in logs:
            function_id, s_or_e, time = log.split(":")

            if s_or_e == "start":
                if call_stack:
                    times[call_stack[-1]] += int(time) - curr_time
                call_stack.append(int(function_id))
                curr_time = int(time)
            else:
                end_id = call_stack.pop()

                times[end_id] += int(time) - curr_time + 1
                curr_time = int(time) + 1
        
        return times