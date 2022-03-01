import collections
class Solution:
    def originalDigits(self, s: str) -> str:
        c = collections.Counter(s)
        
        res = ""
        res += "0"*c['z']
        res += "1"*(c['o'] - c['z'] - c['w'] - c['u'])
        res += "2"*( c['w'] )
        res += "3"*( c['h'] - c['g'] )
        res += "4"*( c['u'] )
        res += "5"*( c['f'] - c['u'] )
        res += "6"*( c['x'] )
        res += "7"*( c['s'] - c['x'] )
        res += "8"*( c['g'] )
        res += "9"*( c['i'] - c['x'] - c['g'] - c['f'] + c['u'] )
        
        return res