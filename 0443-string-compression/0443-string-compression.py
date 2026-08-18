class Solution:
    def compress(self, chars: List[str]) -> int:
        count=1
        ans=""
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                count+=1
            else:
                if count==1:
                    ans+=chars[i]
                else:
                    ans+=chars[i]+str(count)
                    count=1
        if count:
            if count==1:
                ans+=chars[-1]
            else:
                ans+=chars[-1]+str(count)
        chars[:]=list(ans)
        
