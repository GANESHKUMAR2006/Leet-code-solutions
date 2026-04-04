class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows==1:
            return encodedText
        n=len(encodedText)
        cols=n//rows
        matrix=[]
        idx=0
        for i in range(rows):
            matrix.append(encodedText[idx:idx+cols])
            idx+=cols
        result=[]
        for start in range(cols):
            i,j=0,start
            while i<rows and j<cols:
                result.append(matrix[i][j])
                i+=1
                j+=1
        return ''.join(result).rstrip()