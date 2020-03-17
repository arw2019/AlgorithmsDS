from functools import lru_cache

class Solution:
   
    def daysInAMonth(self, month: int, year: int=1) -> int:
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        else: # february
            if year % 4 != 0: return 28
            elif year % 100 != 0: return 29
            elif year % 400 != 0: return 28
            else: 
                return 29
            
    @lru_cache()
    def daysUntil(self, month, year):
        return sum(self.daysInAMonth(m, year) for m in range(month))
    
    def daysFrom1900(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        return 365*(year-2019) + self.daysUntil(month, year) + day
       
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        print(self.daysFrom1900(date1), self.daysFrom1900(date2))
        return abs(self.daysFrom1900(date1) - self.daysFrom1900(date2))
