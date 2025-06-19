import numpy as np
import random

# Environment setup
road_length = 5  # Positions: 0 to 4
actions = 3      # 0 = Left, 1 = Stay, 2 = Right
START_POSITION = 0
GOAL_POSITION = road_length - 1
OBSTACLE_POSITION = 2  # Example obstacle requiring the Right → Left → Right behavior

# Initialize Q-table
Q = np.zeros((road_length, actions))

# Learning parameters
episodes = 500
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3

# Training loop
for episode in range(episodes):
    state = START_POSITION
    done = False

    while not done:
        # Epsilon-greedy policy
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit

        # Perform the action
        if action == 0:      # Move Left
            next_state = max(0, state - 1)
        elif action == 1:    # Stay
            next_state = state
        else:                # Move Right
            next_state = min(road_length - 1, state + 1)

        # Rewards
        if next_state == OBSTACLE_POSITION:
            reward = -5   # Obstacle → penalty
        elif next_state == GOAL_POSITION:
            reward = 10   # Reached the goal
            done = True
        else:
            reward = -1   # Normal step

        # Q-learning update
        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[next_state]) - Q[state, action])

        state = next_state

# Display Q-table
print("\nFinal Q-table (3 actions: Left, Stay, Right):")
print(Q)

# Test the trained agent
state = START_POSITION
steps = 0
print("\n Agent Path (with Right → Left → Right behavior):")

while state != GOAL_POSITION and steps < 20:
    action = np.argmax(Q[state])
    if action == 0:
        next_state = max(0, state - 1)
        move = "Left"
    elif action == 1:
        next_state = state
        move = "Stay"
    else:
        next_state = min(road_length - 1, state + 1)
        move = "Right"

    print(f"Step {steps}: Position {state} → {move} → Next: {next_state}")
    state = next_state
    steps += 1

if state == GOAL_POSITION:
    print(f"\n Successfully crossed the road in {steps} steps.")
else:
    print("\n Failed to cross the road.")