class Skiplist:

    def __init__(self):
        self.arr=[]
    def search(self, target: int) -> bool:
        if target in self.arr:
            return True
        return False
    def add(self, num: int) -> None:
        self.arr.append(num)
    def erase(self, num: int) -> bool:
        if num in self.arr:
            self.arr.remove(num)
            return True
        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)