class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for i in strs:
            s=''.join(sorted(i))
            if s not in mp:
                mp[s]=[]
            mp[s].append(i)
        return [value for value in mp.values()]