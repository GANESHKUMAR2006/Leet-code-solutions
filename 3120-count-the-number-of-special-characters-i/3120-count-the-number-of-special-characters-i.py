class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper=[]
        lower=[]
        for i in word:
            if i.isupper():
                upper.append(i)
            else:
                lower.append(i)
        upper=list(set(upper))
        lower=list(set(lower))
        length=len(upper)
        char=upper
        if length>len(lower):
            length=len(lower)
            char=lower
        count=0
        for i in range(length):
            if char!=upper:
                if char[i].upper() in upper:
                    count+=1
            elif char!=lower:
                if char[i].lower() in lower:
                    count+=1
        return count 