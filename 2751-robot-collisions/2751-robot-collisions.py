class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots=list(zip(positions,healths,directions,range(len(positions))))
        robots.sort()
        stack=[]
        alive=[True]*len(robots)
        for i in range(len(robots)):
            pos,health,dir,idx=robots[i]
            if dir=='R':
                stack.append(i)
            else:
                while stack:
                    top=stack[-1]
                    if not alive[top]:
                        stack.pop()
                        continue
                    if robots[top][1]<robots[i][1]:
                        alive[top]=False
                        robots[i]=(pos,robots[i][1]-1,dir,idx)
                        stack.pop()
                    elif robots[top][1]>robots[i][1]:
                        alive[i]=False
                        robots[top]=(robots[top][0],robots[top][1]-1,robots[top][2],robots[top][3])
                        break
                    else:
                        alive[top]=False
                        alive[i]=False
                        stack.pop()
                        break
        result=[]
        survivors=[]
        for i in range(len(robots)):
            if alive[i]:
                survivors.append((robots[i][3],robots[i][1]))
        survivors.sort()
        for _,health in survivors:
            result.append(health)
        return result