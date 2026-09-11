class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count=0
        for a in range(1,10):
            for b in range(10):
                for c in range(10):
                    if c%2!=0:
                        continue
                    need=[a,b,c]
                    if all(need.count(d)<=digits.count(d) for d in set(need)):
                        count+=1
        return count