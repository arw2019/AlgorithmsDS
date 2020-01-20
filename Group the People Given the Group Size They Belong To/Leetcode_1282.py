from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people_by_gs= defaultdict(list)
        for personId, groupSize in enumerate(groupSizes):
            people_by_gs[groupSize].append(personId)
        ans = []
        for  groupSize, people in people_by_gs.items():
            while people:
                newGroup = []
                for _ in range(groupSize):
                    newGroup.append(people.pop())
                # print(f'new group: {newGroup}')
                ans.append(newGroup)
        return ans
