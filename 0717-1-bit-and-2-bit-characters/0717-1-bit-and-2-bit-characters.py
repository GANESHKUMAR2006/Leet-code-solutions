class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        lp=0
        while lp<len(bits)-1:
            if bits[lp]==1:
                lp+=2
            else:
                lp+=1
        return lp+1==len(bits)