import math
import random
import time

# Nim game class representing the state and rules of the game


class Nim():

    def __init__(self, initial=[1, 3, 5, 7]):
        # Initialize game with given pile configuration
        self.piles = initial.copy()
        self.player = 0  # Player 0 starts the game
        self.winner = None  # No winner at the start

    @classmethod
    def available_actions(cls, piles):
        # Generate all possible actions for the given pile configuration
        actions = set()
        for i, pile in enumerate(piles):
            for j in range(1, pile + 1):
                actions.add((i, j))  # Action is a tuple (pile_index, number_to_remove)
        return actions

    @classmethod
    def other_player(cls, player):
        # Switch to the other player
        return 0 if player == 1 else 1

    def switch_player(self):
        # Switch the current player
        self.player = Nim.other_player(self.player)

    def move(self, action):
        pile, count = action

        # Check if the game has already been won
        if self.winner is not None:
            raise Exception("Game already won")
        # Check if the action is valid
        elif pile < 0 or pile >= len(self.piles):
            raise Exception("Invalid pile")
        elif count < 1 or count > self.piles[pile]:
            raise Exception("Invalid number of objects")

        # Execute the move
        self.piles[pile] -= count
        self.switch_player()

        # Check if the game is won (all piles are empty)
        if all(pile == 0 for pile in self.piles):
            self.winner = self.player

# NimAI class representing the AI player


class NimAI():

    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q = dict()  # Q-values for state-action pairs
        self.alpha = alpha  # Learning rate
        self.epsilon = epsilon  # Exploration rate

    def update(self, old_state, action, new_state, reward):
        # Update Q-values based on the transition from old_state to new_state after action
        old = self.get_q_value(old_state, action)
        best_future = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old, reward, best_future)

    def get_q_value(self, state, action):
        # Get Q-value for a given state-action pair, default to 0 if not found
        return self.q.get((tuple(state), action), 0)

    def update_q_value(self, state, action, old_q, reward, future_rewards):
        # Update Q-value using the Q-learning formula
        new_q = old_q + self.alpha * ((reward + future_rewards) - old_q)
        self.q[(tuple(state), action)] = new_q

    def best_future_reward(self, state):
        # Find the highest Q-value for all possible actions from the given state
        possible_actions = Nim.available_actions(state)
        if not possible_actions:
            return 0

        max_reward = float('-inf')
        for action in possible_actions:
            q_value = self.get_q_value(state, action)
            if q_value > max_reward:
                max_reward = q_value

        return max_reward if max_reward != float('-inf') else 0

    def choose_action(self, state, epsilon=True):
        # Choose an action based on epsilon-greedy policy
        available_moves = list(Nim.available_actions(state))

        # Explore with probability epsilon, exploit otherwise
        if not epsilon or random.random() >= self.epsilon:
            best_action = max(available_moves, key=lambda action: self.get_q_value(
                state, action), default=random.choice(available_moves))
        else:
            best_action = random.choice(available_moves)
        
        return best_action

# Function to train the AI by playing against itself


def train(n):
    player = NimAI()

    for i in range(n):
        print(f"Playing training game {i + 1}")
        game = Nim()

        # Track the last state and action for each player
        last = {
            0: {"state": None, "action": None},
            1: {"state": None, "action": None}
        }

        while True:
            state = game.piles.copy()
            action = player.choose_action(game.piles)

            last[game.player]["state"] = state
            last[game.player]["action"] = action

            game.move(action)
            new_state = game.piles.copy()

            if game.winner is not None:
                # Update Q-values when the game is over
                player.update(state, action, new_state, -1)
                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    1
                )
                break
            elif last[game.player]["state"] is not None:
                # Update Q-values for intermediate steps
                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    0
                )

    print("Done training")
    return player

# Function to play a game against the trained AI


def play(ai, human_player=None):
    if human_player is None:
        human_player = random.randint(0, 1)

    game = Nim()

    while True:
        print()
        print("Piles:")
        for i, pile in enumerate(game.piles):
            print(f"Pile {i}: {pile}")
        print()

        available_actions = Nim.available_actions(game.piles)
        time.sleep(1)

        if game.player == human_player:
            print("Your Turn")
            while True:
                try:
                    pile = int(input("Choose Pile: "))
                    count = int(input("Choose Count: "))
                    if (pile, count) in available_actions:
                        break
                    print("Invalid move, try again.")
                except ValueError:
                    print("Invalid input, enter numerical values.")

        else:
            print("AI's Turn")
            pile, count = ai.choose_action(game.piles, epsilon=False)
            print(f"AI chose to take {count} from pile {pile}.")

        game.move((pile, count))

        if game.winner is not None:
            print()
            print("GAME OVER")
            winner = "Human" if game.winner == human_player else "AI"
            print(f"Winner is {winner}")
            return
