class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log.split())
        
        letter_logs = sorted(letter_logs, key=lambda x:x[0])
        letter_logs = sorted(letter_logs, key=lambda x:x[1:])
        
        for i in range(len(letter_logs)):
            letter_logs[i] = (" ".join(letter_logs[i]))
        
        return letter_logs + digit_logs