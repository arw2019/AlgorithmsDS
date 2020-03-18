import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = tuple(map(int, date1.split('-')))
        date2 = tuple(map(int, date2.split('-')))
        diff = date(*date1) - date(*date2)
        return abs(diff.days)
