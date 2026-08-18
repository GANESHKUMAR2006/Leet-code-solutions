class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        mp={
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        ans=[]
        def backtrack(idx,res):
            if idx==len(digits):
                ans.append(res)
                return
            for letter in mp[int(digits[idx])]:
                backtrack(idx+1,res+letter)
        backtrack(0,'')
        return ans