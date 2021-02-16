import random
import numpy as np 

class QAgent:
    def __init__(self):
        self.q_table = np.zeros((5,7,4)) # q 밸류를 저장하는 변수, 모두 0으로 초기화
        self.eps = 0.9 # 초기에 여기저기 움직여 볼 수 있도록 입실론 값을 크게 해줌
        self.alpha = 0.01

    def select_action(self, s):
        # eps-greedy로 액션 선택
        # s 는 state
        x, y = s 
        coin = random.random() # 0~1사이 값 랜덤
        # esp
        if coin < self.eps:
            action = random.randint(0,3)
        else:
        # 1 - eps / greedy    
            action_val = self.q_table[x,y,:]
            action = np.argmax(action_val)
        return action
    
    def update_table(self, history):
        # 한 에피소드에 해당하는 history를 입력으로 받아 q테이블의 값을 업데이트
        cum_reward = 0 
        for transition in history[::-1]:
            s, a, r, s_prime = transition
            x, y = s 
            # MC를 이용하여 업데이트
            self.q_table[x,y,a] = self.q_table[x,y,a] + self.alpha * (cum_reward - self.q_table[x,y,a])
            cum_reward = cum_reward + r

    def anneal_eps(self):
        self.eps -= 0.03
        self.eps = max(self.eps, 0.1) # 0.1이하로는 ㄴㄴ
    
    def show_table(self):
        # 학습이 각 위치에서 어느 액션의 q 값이 가장 높았는지 보여주는 함수
        q_lst = self.q_table.tolist()
        data = np.zeros((5,7))
        for row_idx in range(len(q_lst)):
            row = q_lst[row_idx]
            for col_idx in range(len(row)):
                col = row[col_idx]
                action = np.argmax(col)
                data[row_idx, col_idx] = action
        print(data)
