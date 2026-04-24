class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        mp=[0]*3
        for i in moves:
            if i=='L':
                mp[0]+=1
            elif i=='R':
                mp[1]+=1
            else:
                mp[2]+=1
        if mp[0]<mp[1]:
            return mp[1]-mp[0]+mp[2]
        else:
            return mp[0]-mp[1]+mp[2]