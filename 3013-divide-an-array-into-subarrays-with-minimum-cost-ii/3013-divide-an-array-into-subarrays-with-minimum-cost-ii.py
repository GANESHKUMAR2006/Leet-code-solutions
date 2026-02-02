from sortedcontainers import SortedList
from typing import List
class Container:
    def __init__(self,k:int):
        self.k=k
        self.small=SortedList()
        self.large=SortedList()
        self.sm=0
    def balance(self):
        while len(self.small)<self.k and self.large:
            x=self.large.pop(0)
            self.small.add(x)
            self.sm+=x
        while len(self.small)>self.k:
            x=self.small.pop()
            self.large.add(x)
            self.sm-=x
    def add(self,x:int):
        if not self.small or x<=self.small[-1]:
            self.small.add(x)
            self.sm+=x
        else:
            self.large.add(x)
        self.balance()
    def erase(self,x:int):
            if x in self.small:
                self.small.remove(x)
                self.sm-=x
            else:
                self.large.remove(x)
            self.balance()
    def sum(self)->int:
        return self.sm
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n=len(nums)
        cnt=Container(k-2)
        for i in range(1,k-1):
            cnt.add(nums[i])
        ans=cnt.sum()+nums[k-1]
        for i in range(k,n):
            out=i-dist-1
            if out>0:
                cnt.erase(nums[out])
            cnt.add(nums[i-1])
            ans=min(ans,cnt.sum()+nums[i])
        return ans+nums[0]