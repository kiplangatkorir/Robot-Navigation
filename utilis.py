import numpy as np
import pickle

def save_model(agent, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(agent.q_table, f)
    print(f"Model saved to {filepath}")

def load_model(agent, filepath):
    with open(filepath, 'rb') as f:
        agent.q_table = pickle.load(f)
    print(f"Model loaded from {filepath}")

def visualize_environment(env):
    for row in env.grid:
        print(' '.join(row))
    print()

def print_q_table(agent):
    print("Q-table:")
    print(agent.q_table)

def plot_rewards(rewards):
    import matplotlib.pyplot as plt

    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('Training Rewards')
    plt.show()
