class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack  = []
        for a in asteroids:
            if not stack or a > 0: 
                stack.append(a)
            elif a < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] + a == 0: 
                        stack.pop()
                        break
                    elif stack[-1] + a < 0:
                        stack.pop()
                        continue
                    elif stack[-1] + a > 0:
                        break
                else:
                    stack.append(a)
        return stack
