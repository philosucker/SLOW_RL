import numpy as np
from agent import Agent
from env import GridWorld


def main():
    env = GridWorld()
    agent = Agent()
    data = np.zeros((4, 4))
    gamma = 1.0
    alpha = 0.0001

    # 5만번 에피소드
    for k in range(50000):
        done = False
        history = []
        # 3,3 에 도달할때까지 계속 실행
        while not done:
            # action이 선택됨
            action = agent.select_action()
            (x, y), reward, done = env.step(action)
            history.append((x, y, reward))
        env.reset()

        # 매 에피소드가 끝나고 바로 해당 데이터를 이용해 테이블을 업데이트
        # 누적 보상
        cum_reward = 0
        # history를 뒤집어서 도착지점부터 거꾸로 보상을 계산해나감
        for transition in history[::-1]:
            x, y, reward = transition
            # 각 스테이트 밸류 계산 조금씩 업데이트 하는 방법
            data[x][y] = data[x][y] + alpha * (cum_reward - data[x][y])
            cum_reward = cum_reward + gamma * reward

    # 학습이 끝나고 데이터를 출력
    for row in data:
        print(row)


if __name__ == "__main__":
    main()