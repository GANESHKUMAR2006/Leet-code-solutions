class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid=["electronics","grocery","pharmacy","restaurant"]
        cateogry={cat: i for i,cat in enumerate(valid)}
        result=[]
        for c,b,a in zip(code,businessLine,isActive):
            if a and b in cateogry and c and all(ch.isalnum() or ch=="_" for ch in c):
                    result.append((cateogry[b],[b],c))
        result.sort()
        return [c for _,_, c in result]