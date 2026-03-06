class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=sum(cardPoints[:k])
        right=0
        maxsum=left
        idx=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            left-=cardPoints[i]
            right+=cardPoints[idx]
            idx-=1
            maxsum=max(maxsum,right+left)
        return maxsum