class Solution:
    def minTimeToType(self, word: str) -> int:
        
        sec = 0
        curr = 'a'
        clock = 0
        counter_clock = 0
        for char in word:
            if ord(curr) <= ord(char):
                clock = ord(char) - ord(curr)
                counter_clock = ord(curr) - ord('a') + ord('z') - ord(char)+1
            else:
                # char < curr
                clock = ord('z') - ord(curr) + ord(char) - ord('a') + 1
                counter_clock = ord(curr) - ord(char)
            curr = char
            sec += min(clock, counter_clock) + 1
        
        return sec