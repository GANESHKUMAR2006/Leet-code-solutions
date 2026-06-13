class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for word in words:
            val=0
            for char in word:
                idx=ord(char)-ord('a')
                val+=weights[idx]
            val=val%26
            ans+=chr(ord('z')-val)
        return ans
                