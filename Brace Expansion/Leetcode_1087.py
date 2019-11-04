class Solution:
    def expand(self, S: str) -> List[str]:
        s = S.replace('{','*').replace('}','*').split('*')
        res = ['']
        for el in s:
            if ',' not in el: res = [x+el for x in res]
            else:
                res = [x+y for x in res for y in el.split(',')]
        return sorted(res)
