# import collections
class Logger:

    def __init__(self):
        self.dic = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dic:
                self.dic[message] = timestamp
                return True
        elif self.dic[message] + 10 > timestamp: return False
        else:
            self.dic[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)