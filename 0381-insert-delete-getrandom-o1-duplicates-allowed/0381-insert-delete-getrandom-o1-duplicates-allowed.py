import random
class RandomizedCollection:

    def __init__(self):
        self.arr=[]
    def insert(self, val: int) -> bool:
        if val in self.arr:
            self.arr.append(val)
            return False
        else:
            self.arr.append(val)
            return True
    def remove(self, val: int) -> bool:
        if self.arr:
            if val in self.arr:
                self.arr.remove(val)
                return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()