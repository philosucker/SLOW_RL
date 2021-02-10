import argparse
import numpy as np
from agent import Agent
from env import GridWorld

def to_str(x):
    if x.lower() == 'mc':
        return 'mc'
    elif x.lower() == 'td':
        return 'td'
    else:
        raise argparse.ArgumentTypeError("you got mc or td")

def mc(data, gamma, alpha, num_ep):
    data = data
    gamma = gamma
    alpha = alpha

    # num_ep번 에피소드
    for k in range(num_ep):
        done = False
        history = []
        # (map_size-1, map_size-1) 에 도달할때까지 계속 실행
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

def td(data, gamma, alpha, num_ep):
    data = data
    gamma = gamma
    alpha = alpha

    # num_ep번 에피소드
    for k in range(num_ep):
        done = False
        while not done:
            x, y = env.get_state()
            action = agent.select_action()
            (x_prime, y_prime), reward, done = env.step(action)
            x_prime, y_prime = env.get_state()

            # 한 번의 step이 진행되면 바로 테이블의 데이터를 업데이트
            data[x][y] = data[x][y] + alpha*(reward+gamma*data[x_prime][y_prime]-\
                                             data[x][y])

        # 한 에피소드가 종료되었으니 환경 설정을 초기세팅으로 돌림
        env.reset()

    # 학습 결과를 출력
    for row in data:
        print(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--alpha", type=float, default=0.0001)
    parser.add_argument("--map_size", type=int, default=4)
    parser.add_argument("--num_ep", type=int, default=50000)
    parser.add_argument("--method", type=to_str, default='mc')

    arg = parser.parse_args()

    # Set hyper-parameters
    gamma = arg.gamma #
    alpha = arg.alpha
    map_size = arg.map_size
    num_ep = arg.num_ep # 에피소드 진행 횟수
    method = arg.method

    env = GridWorld()
    agent = Agent()

    data = np.zeros((map_size, map_size))

    if method == 'mc':
        mc(data, gamma, alpha, num_ep)
    elif method == 'td':
        print(data, gamma, alpha, num_ep, method)
        td(data, gamma, alpha, num_ep)
