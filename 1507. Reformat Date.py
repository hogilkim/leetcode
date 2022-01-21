# solved
# first attempt - Jan 21, 2022
class Solution:
    def reformatDate(self, date: str) -> str:
        mon_to_digit={"Jan":"01","Feb": "02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        year = date[-4:]
        
        month = mon_to_digit[date[-8:-5]]
        day = date[:-11]
        if len(day) ==1:
            day = '0'+day
        return year+'-'+month+'-'+day