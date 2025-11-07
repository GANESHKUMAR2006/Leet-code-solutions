class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[0]*(num_people)
        i=0
        cnt=1
        while candies:
            if candies<cnt:
                cnt=candies
            if i==num_people:
                i=0
            ans[i]+=cnt
            candies-=cnt
            i+=1
            cnt+=1
        return ans