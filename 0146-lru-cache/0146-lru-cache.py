from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.mp={}
        self.dq=deque()
    def get(self, key: int) -> int:
        if key in self.mp:
            self.dq.remove(key)
            self.dq.appendleft(key)
            return self.mp[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key]=value
            self.dq.remove(key)
            self.dq.appendleft(key)
        else:
            if len(self.mp)>=self.cap:
                mainkey=self.dq.pop()
                del self.mp[mainkey]
            self.mp[key]=value
            self.dq.appendleft(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)