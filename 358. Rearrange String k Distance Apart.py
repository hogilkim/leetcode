class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k: return s
        
        counter = collections.Counter(s)
        max_heap = []
        for key in counter.keys():
            max_heap.append([-counter[key], key])
        
        heapq.heapify(max_heap)
        result = ""
        
        while max_heap:
            chars_to_putback=[]
            for i in range(k):
                if max_heap:
                    char_num, char = heapq.heappop(max_heap)
                    result += char
                    char_num += 1
                    if char_num < 0:
                        chars_to_putback.append([char_num, char])
                # nothing more to add - finished
                elif not chars_to_putback:
                    break;
                # not reached 'k' but still has sth to add - cannot make k distance apart
                else:
                    return ""
            
            for char_num, char in chars_to_putback:
                heapq.heappush(max_heap, [char_num, char])
        
        
        return result