class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq=Counter(s)
        n=len(s)
        i=0
        while i<n and freq[target[i]]>0:
            freq[target[i]]-=1
            i+=1
        while i>=0:
            if i<n:
                for ch in map(chr,range(ord(target[i])+1,ord('z')+1)):
                    if freq[ch]>0:
                        ans=target[:i]+ch
                        freq[ch]-=1
                        for c in sorted(freq):
                            ans+=c*freq[c]
                        return ans
            i-=1
            if i>=0:
                freq[target[i]]+=1
        return ""
