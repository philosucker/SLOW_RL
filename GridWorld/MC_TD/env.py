class GridWorld:
    # 4 x 4 그리드 월드
    x = 0
    y = 0

    def step(self, a):
        if a == 0:
            self.move_right()
        elif a == 1:
            self.move_left()
        elif a == 2:
            self.move_up()
        else:
            self.move_down()

        # 보상은 언제나 -1
        reward = -1
        done = self.is_done()
        return (self.x, self.y), reward, done

    def move_right(self):
        # 오른쪽으로 이동하니까 y좌표 +1
        self.y += 1

        if self.y > 3:
            # 가장 오른쪽 칸을 벗어나려고 하면 가장 오른쪽 칸으로 돌아온다
            self.y = 3

    def move_left(self):
        # 왼쪽으로 이동하니까 x좌표 -1
        self.y -= 1

        if self.y < 0:
            # 가장 왼쪽 칸을 벗어나려고 하면 가장 왼쪽 칸으로 돌아온다
            self.y = 0

    def move_up(self):
        # 위로 움직이니까 x좌표 -1
        self.x -= 1

        if self.x < 0:
            # 맨 위를 뚫으려고하면 맨 위로 다시 돌아온다
            self.x = 0

    def move_down(self):
        # 아래로 움직이니까 x좌표 +1
        self.x += 1

        if self.x > 3:
            # 맨 아래를 뚫으려고하면 맨 아래로 다시 돌아온다
            self.x = 3

    def is_done(self):
        # x,y 가 3,3 이 되면 에피소드 종료
        if self.x == 3 and self.y == 3:
            return True
        else:
            return False

    def get_state(self):
        return (self.x, self.y)

    def reset(self):
        # 에피소드가 끝나면 0,0 위치로 다시 돌아감
        self.x = 0
        self.y = 0
        return (self.x, self.y)