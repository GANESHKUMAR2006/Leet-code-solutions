class Solution:
    def bitwiseComplement(self, n: int) -> int:
        val=format(n,'b')
        ans=''
        for i in val:
            if i=='1':
                ans+='0'
            else:
                ans+='1'
        return int(ans,2)