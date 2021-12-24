class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        
        return letters[0]


# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         answer = "z"
#         updated = False
#         for letter in letters:
#             if letter > target:
#                 answer = min(answer, letter)
#                 updated = True
        
#         return answer if updated else min(letters)