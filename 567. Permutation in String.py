class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = [0] * 26
        s2_list = [0] * 26
        
        for char in s1:
            s1_list[ord(char) - ord('a')] += 1

        for i in range(len(s2)):   
            s2_list[ord(s2[i]) - ord('a')] += 1
            
            if i >= len(s1):
                s2_list[ord(s2[i-len(s1)]) - ord('a')] -= 1
            print(s2_list)
            if s1_list == s2_list:
                return True
            
        return False
            
            
            
#         if len(s1) > len(s2):
#             return False
#         l, r = 0, len(s1)-1
        
#         alphabet = 'a'
#         s2_substring = {}
#         s2_substring = dict.fromkeys(string.ascii_lowercase, 0)       
        
#         for j in range(len(s1)-1):
#             s2_substring[s2[j]] += 1
#         s1_counter = Counter(s1)
#         print(s1_counter)
#         while r < len(s2):
#             s2_substring[s2[r]] += 1
#             # print(s2_substring)
#             if all(s2_substring[key]==val for key, val in s1_counter.items()):
#                 return True
            
#             s2_substring[s2[l]] -= 1
#             l+=1
#             r+=1
#         return False