class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        dp = [0]*len(books)
        stack = []
        
        for i in range(len(books)):
            if books[i] == 0:
                stack.append(i); continue;
                
            while stack:
                j = stack[-1]
                if books[j] >= books[i] - (i-j):
                    stack.pop()
                else:
                    break
                    
            if not stack:
                j = -1
            
            # ----
            if books[i] - i + j + 1 < 0:
                dp[i] = books[i] * (books[i] + 1)//2
            else:
                dp[i] = (books[i] + books[i] - i + j + 1) * (i - j) // 2
            
            if j >= 0:
                dp[i] += dp[j]
            
            stack.append(i)
        
        return max(dp)