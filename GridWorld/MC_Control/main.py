from .env import GridWorld
from .agent import QAgent

def main():
    env = GridWorld()
    agent = QAgent()

    for n_epi in range(1000): # 1000 episode 
        done = False 
        history = []

        s = env.reset()
        while not done:# 한 에피소드가 끝날 때까지
            a = agent.select_action(s)
            s_prime, r, done = env.step(a)
            history.append((s, a, r, s_prime))
            s = s_prime
        agent.update_table(history) # 히스토리 이용하여 에이전드 업데이트
        agent.anneal_eps()
    
    agent.show_table() # 학습 끝난 결과 출력

if __name__ == "__main__":
    main()


