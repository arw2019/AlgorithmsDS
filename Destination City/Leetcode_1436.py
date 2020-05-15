class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities, outgoing = set(), set()
        for source, dest in paths:
            cities |= {source} | {dest}
            outgoing |= {source}
        return (cities-outgoing).pop()
