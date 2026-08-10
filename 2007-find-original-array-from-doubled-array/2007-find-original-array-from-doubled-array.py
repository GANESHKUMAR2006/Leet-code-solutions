class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        freq=Counter(changed)
        changed.sort()
        original=[]
        for num in changed:
            if freq[num]==0:
                continue
            if freq[num*2]==0:
                return []
            original.append(num)
            freq[num]-=1
            freq[num*2]-=1
        return original