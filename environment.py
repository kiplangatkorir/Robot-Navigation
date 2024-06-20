import numpy as np

class RobotEnvironment:
    def __init__(self, grid_size=(5, 5), start=(0, 0), goal=(4, 4)):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.current_position = start
        self.obstacles = [(2, 2), (3, 3)]  # Example obstacles

    def reset(self):
        self.current_position = self.start
        return self.current_position

    def step(self, action):
        # Define possible actions: 0 - up, 1 - down, 2 - left, 3 - right
        if action == 0:
            new_position = (self.current_position[0] - 1, self.current_position[1])
        elif action == 1:
            new_position = (self.current_position[0] + 1, self.current_position[1])
        elif action == 2:
            new_position = (self.current_position[0], self.current_position[1] - 1)
        elif action == 3:
            new_position = (self.current_position[0], self.current_position[1] + 1)
        else:
            raise ValueError("Invalid action")

        # Check if new position is within bounds and not an obstacle
        if self._is_within_bounds(new_position) and self._is_not_obstacle(new_position):
            self.current_position = new_position
        
        # Determine reward and done status
        reward = self._calculate_reward()
        done = self.current_position == self.goal

        return self.current_position, reward, done

    def _is_within_bounds(self, position):
        return 0 <= position[0] < self.grid_size[0] and 0 <= position[1] < self.grid_size[1]

    def _is_not_obstacle(self, position):
        return position not in self.obstacles

    def _calculate_reward(self):
        if self.current_position == self.goal:
            return 1.0  # Positive reward upon reaching the goal
        elif self.current_position in self.obstacles:
            return -1.0  # Negative reward for hitting an obstacle
        else:
            return 0.0

    def render(self):
        grid = np.zeros(self.grid_size, dtype=str)
        grid[self.current_position] = 'R'  # R represents the robot's current position
        grid[self.goal] = 'G'  # G represents the goal position
        for obstacle in self.obstacles:
            grid[obstacle] = 'X'  # X represents obstacles
        print(grid)

# Example usage
if __name__ == "__main__":
    env = RobotEnvironment()
    env.render()
    print("Initial position:", env.current_position)
    action = 3  # Move right
    next_position, reward, done = env.step(action)
    env.render()
    print("Next position:", next_position)
    print("Reward:", reward)
    print("Done:", done)
