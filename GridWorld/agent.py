import random


class Agent:
    def select_action(self):
        coin = random.random()  # 0~1 사이 값을 랜덤으로 뽑는다
        # 동서남북으로 움직이는 액션을 취할 확률은 .25로 같다
        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action = 2
        else:
            action = 3

        return action
