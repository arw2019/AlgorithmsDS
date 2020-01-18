import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        if len(houses) == 1: 
            return min(abs(heater_location - houses[0]) for heater_location in heaters)
        
        heaters.sort()
        houses.sort()
        
        closest_heater = [0]*len(houses)
        
        for i, house_location in enumerate(houses):
            idx = bisect.bisect_left(heaters, house_location)
            if idx == 0:
                closest_heater[i] = heaters[0] - house_location
            elif idx == len(heaters):
                closest_heater[i] = house_location - heaters[-1]
            else:
                l = house_location - heaters[idx-1]
                r = heaters[idx] - house_location
                closest_heater[i] = l if l <= r else r
                        
        return max(closest_heater)
