class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        numrow=[[1]]
        for i in range(numRows-1):
            result=[]
            trick=[0]+numrow[-1]+[0]
            for j in range(len(trick)-1):
                result.append(trick[j]+trick[j+1])
            numrow.append(result)
        return numrow