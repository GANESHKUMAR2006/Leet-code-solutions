class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour%=12
        ha=30*hour+0.5*minutes
        ma=6*minutes
        diff=abs(ha-ma)
        return min(diff,360-diff)