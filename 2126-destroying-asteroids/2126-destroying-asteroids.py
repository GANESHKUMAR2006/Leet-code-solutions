class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        stack=[mass]
        for i in range(len(asteroids)):
            if stack[-1]<asteroids[i]:
                return False
            else:
                stack[-1]+=asteroids[i]
        return True