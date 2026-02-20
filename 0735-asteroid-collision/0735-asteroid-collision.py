class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            alive=True
            while alive and stack and stack[-1]>0 and asteroids[i]<0:
                if abs(stack[-1])<abs(asteroids[i]):
                    stack.pop()
                    continue
                elif abs(stack[-1])==abs(asteroids[i]):
                    stack.pop()
                    alive=False
                else:
                    alive=False
            if alive:
                stack.append(asteroids[i])
        return stack
