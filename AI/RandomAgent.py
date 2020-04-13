from Entities.State import State
from Game import GameLogic
import random


class RandomAgent:

    def actions(self, state: State):
        temp_val = GameLogic.list_available_pits(state)
        return temp_val

    def random_action(self, state: State):
        options = self.actions(state)
        return random.choice(options)
