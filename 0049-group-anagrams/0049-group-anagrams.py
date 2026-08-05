class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for i in strs:
            s=''.join(sorted(i))
            mp[s].append(i)
        return [value for value in mp.values()]