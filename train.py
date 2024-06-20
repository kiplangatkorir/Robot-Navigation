from environment import RobotEnvironment
from agent import QLearningAgent

def train_agent(env, agent, episodes=1000):
    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        step = 0

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update_q_table(state, action, reward, next_state)
            state = next_state
            total_reward += reward
            step += 1

        print(f"Episode {episode + 1}/{episodes} completed with total reward: {total_reward} in {step} steps.")

# Example usage
if __name__ == "__main__":
    env = RobotEnvironment()
    agent = QLearningAgent(num_actions=4)  


    train_agent(env, agent)
    print("Training completed.")

