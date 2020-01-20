from collections import defaultdict, Counter
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people_by_gs= defaultdict(list)
        for personId, groupSize in enumerate(groupSizes):
            people_by_gs[groupSize].append(personId)
        ans = []
        for groupSize in set(groupSizes):
            while people_by_gs[groupSize]:
                newGroup = []
                curSize = people_by_gs[groupSize]
                for _ in range(groupSize):
                    newGroup.append(curSize.pop())
                # print(f'new group: {newGroup}')
                ans.append(newGroup)
        return ans
