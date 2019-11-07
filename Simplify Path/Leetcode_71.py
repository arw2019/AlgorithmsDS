import string
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for s in path.split('/'):
            if s == '..' and stack:
                stack.pop()
            elif s and s not in ('.', '..'):
                stack.append(s)
        return "".join('/' + s for s in stack) if stack else "/"
