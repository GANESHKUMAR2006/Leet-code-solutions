class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        box=[[1]]
        for i in range(rowIndex):
            new=[0]+box[-1]+[0]
            result=[]
            for j in range(len(new)-1):
                result.append(new[j]+new[j+1])
            box.append(result)
        return box[rowIndex]