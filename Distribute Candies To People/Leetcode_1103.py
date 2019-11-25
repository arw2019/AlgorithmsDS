class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        num_candies, person, tot = 1, 0, candies
        while True:
            person %= num_people
            if num_candies > tot: 
                res[person] += tot
                break
            res[person] += num_candies
            tot -= num_candies
            num_candies += 1
            person += 1
        return res