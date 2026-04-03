class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n=len(robots)
        left=[0]*n
        right=[0]*n
        num=[0]*n
        dis={}
        for i in range(n):
            dis[robots[i]]=distance[i]
        robots.sort()
        walls.sort()
        for i in range(n):
            pos1=bisect.bisect_right(walls,robots[i])
            if i>=1:
                left_bound=max(robots[i]-dis[robots[i]],robots[i-1]+1)
                leftpos=bisect.bisect_left(walls,left_bound)
            else:
                leftpos=bisect.bisect_left(walls,robots[i]-dis[robots[i]])
            left[i]=pos1-leftpos
            if i<n-1:
                right_bound=min(robots[i]+dis[robots[i]],robots[i+1]-1)
                rightpos=bisect.bisect_right(walls,right_bound)
            else:
                rightpos=bisect.bisect_right(walls,robots[i]+dis[robots[i]])
            pos2=bisect.bisect_left(walls,robots[i])
            right[i]=rightpos-pos2
            if i==0:
                continue
            pos3=bisect.bisect_left(walls,robots[i-1])
            num[i]=pos1-pos3
        sub_left,sub_right=left[0],right[0]
        for i in range(1,n):
            current_left=max(sub_left+left[i],sub_right-right[i-1]+min(left[i]+right[i-1],num[i]))
            current_right=max(sub_left+right[i],sub_right+right[i])
            sub_left,sub_right=current_left,current_right
        return max(sub_left,sub_right)