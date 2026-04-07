class Robot:

    def __init__(self, width: int, height: int):
        self.w=width
        self.h=height
        self.x=0
        self.y=0
        self.dir=0
        self.dirs=['East','North','West','South']
        self.moves=[(1,0),(0,1),(-1,0),(0,-1)]
        self.perimeter=2*(width+height-2)
    def step(self, num: int) -> None:
        num%=self.perimeter
        if num==0:
            num=self.perimeter
        while num>0:
            dx,dy=self.moves[self.dir]
            nx,ny=self.x+dx,self.y+dy
            if not(0<=nx<self.w and 0<=ny<self.h):
                self.dir=(self.dir+1)%4
            else:
                self.x,self.y=nx,ny
                num-=1

    def getPos(self) -> List[int]:
        return [self.x,self.y]

    def getDir(self) -> str:
        return self.dirs[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()