class GridWorld:
    def __init__(self):
        # 좌표
        self.x = 0
        self.y = 0
    
    def step(self, a):
        # 0 ~ 3 왼 위 오 아
        if a == 0:
            self.move_left()
        elif a ==1:
            self.move_up()
        elif a == 2:
            self.move_right()
        elif a ==3:
            self.move_down()
        
        reward = -1
        done = self._is_done()
        return (self.x, self.y), reward, done
    
    def move_right(self):
        if self.y ==1 and self.x in (0,1,2):
            pass 
        elif self.y == 3 and self.x in (2,3,4):
            pass 
        elif self.y == 6:
            pass
        else:
            self.y +=1
        
    def move_up(self):
        if self.x == 1:
            pass
        elif self.x == 3 and self.y ==2:
            pass 
        else:
            self.x -= 1

    def move_left(self):
        if self.y ==0:
            pass 
        elif self.y ==3 and self.x in (0,1,2):
            pass
        elif self.y ==5 and self.x in (2,3,4):
            pass 
        else:
            self.y -= 1
    
    def move_down(self):
        if self.x == 4:
            pass
        elif self.x == 1 and self.y ==4:
            pass 
        else:
            self.x += 1
    
    def _is_done(self):
        if self.x == 4 and self.y ==6:
            return True    
        return False
    
    def reset(self):
        self.x = 0 
        self.y = 0 
        return (self.x, self.y)