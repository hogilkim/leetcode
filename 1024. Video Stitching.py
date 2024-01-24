# Solve again Jan 24, 2024 1024
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips, key=lambda x:(x[0], x[1]))
        num_clips = 0
        curr_end_time = 0
        i = 0

        while i < len(clips):
            if clips[i][0] > curr_end_time: return -1

            max_end_time = curr_end_time
            while i < len(clips) and clips[i][0] <= curr_end_time:
                max_end_time = max(max_end_time, clips[i][1])
                i += 1
            
            num_clips += 1
            curr_end_time = max_end_time

            if curr_end_time >= time: return num_clips
        
        return -1


        ## Another Solution
        # clips = sorted(clips, key=lambda x:(x[0], x[1]))
        # stack = [(0,0)]

        # for start, end in clips:
        #     print(stack)
            
        #     while len(stack) > 1 and stack[-2][1] >= start and stack[-1][1] < end:
        #         stack.pop()
        #     if stack[-1][1] < start: break
        #     if end >= time: return len(stack)
        #     stack.append((start, end))
            
        # return -1

        ## This also passed
        # clips = sorted(clips, key=lambda x:(x[0], x[1]))
        # if clips[0][0] > 0: return -1
        # if clips[0][1] >= time: return 1
        # stack = [clips[0]]

        # for start, end in clips[1:]:
        #     if stack[-1][1] >= end: continue
        #     if start > stack[-1][1]: return -1

        #     if stack[-1][0] == start:
        #         stack.pop()
        #         stack.append([start, end])
            
        #     elif len(stack) >= 2 and start <= stack[-2][1]:
        #             stack.pop()
        #             stack.append([start,end])
            
        #     else:
        #         stack.append([start, end])
            
        #     if end >= time: break
        # return len(stack) if end >= time else -1