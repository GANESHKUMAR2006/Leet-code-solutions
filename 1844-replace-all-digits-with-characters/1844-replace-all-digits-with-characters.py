class Solution:
    def replaceDigits(self, s: str) -> str:
        char=[]
        for i in s:
            if i.isdigit():
                val=chr(ord(char[-1])+int(i))
                char.append(val)
            else:
                char.append(i)
        return ''.join(char)