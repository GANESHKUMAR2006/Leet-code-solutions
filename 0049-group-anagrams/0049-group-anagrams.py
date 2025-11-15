class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset=defaultdict(list)
        for i in strs:
            count=[0]*(26)
            for ch in i:
                count[ord(ch)-ord('a')]+=1
            hashset[tuple(count)].append(i)
        return [values for values in hashset.values()]