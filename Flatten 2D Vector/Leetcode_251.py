class Vector2D:

    def __init__(self, v: List[List[int]]):
        
        self.row = 0
        self.column = 0
        self.vector = v

    def next(self) -> int:
        if self.hasNext():
            entry = self.vector[self.row][self.column]
            self.column += 1
            return entry
        else:
            raise ValueError("End of vector.")
        

    def hasNext(self) -> bool:
        while self.row < len(self.vector):
            while self.column < len(self.vector[self.row]):
                return True
            self.row += 1
            self.column = 0
        return False
        
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()