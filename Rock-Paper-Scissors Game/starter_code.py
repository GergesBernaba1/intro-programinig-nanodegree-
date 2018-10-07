#!/usr/bin/env python3
from random import randint
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):

        return random_move()


class HumanPlayer(Player):
    def move(self):
        value = input("Please enter your move"
                      "(Only rock, scissors or paper is allowed.)\n")
        value = value.lower()
        if valid_move(value) or value == "quit":
            return value
        else:
            print("Wrong input format!")

            return self.move()


class ReflectPlayer(Player):
    def __init__(self):
        self.next_move = random_move()

    def learn(self, my_move, their_move):
        self.next_move = their_move

    def move(self):
        return self.next_move


class CyclePlayer(Player):
    def __init__(self):
        self.move_idx = 0

    def move(self):
        current_move = moves[self.move_idx]
        self.move_idx = (self.move_idx + 1) % 3
        return current_move


class RepeatPlayer(Player):
    def __init__(self):
        self.next_move = random_move()

    def move(self):
        return self.next_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def random_move():
    return moves[randint(0, 2)]


def valid_move(value):
    return value in moves


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = self.p2_score = 0
        self.game_count = 1

    def display_scoreboard(self):
        print("\n\tScore\nPlayer 1: | Player 2:\n   {0}           {1}".format(
            self.p1_score, self.p2_score)
        )

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 == "quit":
            return False
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("Player 1 wins!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 wins!")
            self.p2_score += 1
        else:
            print("This is a tie!")
        self.display_scoreboard()
        return True

    def play_game(self):
        print("\nGame start!\nNote that you are always Player 1.")
        while True:
            print(f"Round {self.game_count}:")
            if not self.play_round():
                break
            self.game_count += 1
        self.display_scoreboard()


if __name__ == '__main__':
    print('Here are the rules of the game: scissor cuts paper,paper covers'
          ' rock, and rock crushes scissors.\nPlay either "rock", "paper",'
          ' or "scissors"\nIf you want to stop playing, enter quit.')
    game_type = None
    while game_type not in ["random", "reflect", "repeat", "cycle"]:
        if game_type is not None:
            print("Enter a valid opponent player type!")
        game_type = input('Who would you like to play with? '
                          'Please enter "random", "reflect", "repeat",'
                          ' or "cycle"\n')
        game_type = game_type.lower()
    if game_type == "random":
        game = Game(HumanPlayer(), RandomPlayer())
    elif game_type == "reflect":
        game = Game(HumanPlayer(), ReflectPlayer())
    elif game_type == "repeat":
        game = Game(HumanPlayer(), RepeatPlayer())
    else:
        game = Game(HumanPlayer(), CyclePlayer())

    game.play_game()
