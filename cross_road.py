import numpy as np
import random

# Environment setup
n_states = 5  # Road has 5 positions: 0 to 4
n_actions = 3  # Actions: 0=Left, 1=Stay, 2=Right

# Initialize Q-table: [states x actions]
Q = np.zeros((n_states, n_actions))

# Hyperparameters
episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3

# Training
for episode in range(episodes):
    state = 0  # Start at position 0
    while state != n_states - 1:
        # Choose action (Epsilon-Greedy)
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, n_actions - 1)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit

        # Take action
        if action == 0:  # Left
            next_state = max(0, state - 1)
        elif action == 1:  # Stay
            next_state = state
        else:  # Right
            next_state = min(n_states - 1, state + 1)

        # Define reward
        if state == 0 and action == 0:
            reward = -10  # Hit wall on the left
        elif state == n_states - 1 and action == 2:
            reward = -10  # Hit wall on the right
        elif next_state == n_states - 1:
            reward = 10  # Goal reached
        else:
            reward = -1  # Step cost

        # Q-learning update
        Q[state, action] += learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action])

        state = next_state

# Show final Q-table
print("\nFinal Q-Table (State x Action [Left, Stay, Right]):")
print(Q)

# Test the agent after training
print("\nAgent's path from start to goal:")
state = 0
steps = 0
while state != n_states - 1:
    action = np.argmax(Q[state])
    if action == 0:
        next_state = max(0, state - 1)
        action_str = "Left"
    elif action == 1:
        next_state = state
        action_str = "Stay"
    else:
        next_state = min(n_states - 1, state + 1)
        action_str = "Right"

    print(f"Step {steps}: State {state} -> {action_str} -> State {next_state}")
    state = next_state
    steps += 1

print(f"Reached goal in {steps} steps.")
