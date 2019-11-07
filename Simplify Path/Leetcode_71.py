#top 5% of submissions
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split('/')
        for directory in dirs:
            if len(directory) > 0:
                if directory == '.': 
                    continue
                elif directory == '..':
                    if stack:
                        del stack[-1]
                else:
                    stack.append(directory)
        print(stack)
        return '/'+'/'.join(stack)
