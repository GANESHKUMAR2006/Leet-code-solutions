class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=format(n,'b')
        for i in range(len(n)-1):
            if((n[i]=="1" and n[i+1]=="0") or(n[i]=="0" and n[i+1]=="1")):
                continue
            else:
                return False
                break
        return True