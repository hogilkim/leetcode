import collections
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = collections.deque(food)
        self.board = [[0]*width]*height
        self.board[0][0] = 1
        self.snake = [(0,0)]
        # snake[0] = tail, snake[-1] = head

    def move(self, direction: str) -> int:
        directions = {"R": (0,1), "D":(1,0), "U": (-1,0), "L": (0,-1)}
        
        new_head = (self.snake[-1][0] + directions[direction][0], self.snake[-1][1] +directions[direction][1])
        if new_head[0] >= len(self.board) or new_head[1] >= len(self.board[0]) or new_head[0] < 0\
        or new_head[1] < 0 or new_head in self.snake[1:]:
            return -1
        
        
        self.snake.append(new_head)
        if self.food and new_head[0] == self.food[0][0] and new_head[1] == self.food[0][1]:
            if self.snake[0] == new_head[0] and self.snake[1] == new_head[1]:
                return -1
            
            self.food.popleft()
            return len(self.snake)-1
        
        self.snake = self.snake[1:]
        return len(self.snake)-1
        
            
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)