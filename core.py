import random
from os import system
from time import sleep

import config
from utils import Colors


class ColoringGame:
    def __init__(self):
        field = []
        for i in range(config.FIELD_SIZE):
            field.append([])
            for j in range(config.FIELD_SIZE):
                field[i].append('O')
        self.field = field

    def print_field(self):
        size = len(self.field)
        border = [i for i in range(size)]

        print('   |', end=' ')
        print(*border, sep=' | ', end=' |\n')
        for i in range(size):
            print('%2d' % border[i], end=' | ')
            for j in range(size):
                symbol = self.field[i][j]
                if symbol != 'O':
                    color = Colors.get_color(symbol)
                    print(color + symbol + Colors.ENDC, end=' ')
                else:
                    print(self.field[i][j], end=' ')
                print('|', end=' ')
            print()

    def start(self):
        player_1_turn_function = self._player_turn
        player_2_turn_function = self._player_turn if config.PLAY_AGAINST == 'player' else self._ai_turn

        first_player_turn = True

        while True:
            system('clear')
            self.print_field()
            player = 1 if first_player_turn else 2
            print(f"Player #{player} turn!")
            if first_player_turn:
                player_1_turn_function()
            else:
                player_2_turn_function()
            if not self._get_valid_choices():
                print(f'GAME OVER. Player #{player} won!')
                break
            first_player_turn = not first_player_turn

    def _get_input(self, valid_choices):
        choice = input()
        params = choice.split(' ')
        try:
            x = int(params[0])
            y = int(params[1])
        except ValueError:
            return False

        choice = (x, y, params[2])
        for valid_choice in valid_choices:
            if x == valid_choice[0] and y == valid_choice[1] and params[2] in valid_choice[2]:
                return choice
        return False

    def _player_turn(self):
        valid_choices = self._get_valid_choices()
        print('Your options')
        print(valid_choices)
        choice = False
        while not choice:
            print('Please, input your choice in valid format: x y color')
            choice = self._get_input(valid_choices)           
        self._process_choice(choice)

    def _ai_turn(self):
        valid_choices = self._get_valid_choices()
        choice_index = random.randint(0, len(valid_choices) - 1)
        choice = valid_choices[choice_index]
        colors = tuple(choice[2])
        color_index = random.randint(0, len(colors) - 1)
        print('AI needs some time to think ...')
        sleep(1.5)
        self._process_choice((choice[0], choice[1], colors[color_index]))


    def _process_choice(self, choice):
        x = choice[0]
        y = choice[1]
        color = choice[2]
        self.field[x][y] = color

    def _get_valid_choices(self):
        size = len(self.field)
        choices = []
        for i in range(size):
            for j in range(size):
                if self.field[i][j] == 'O':
                    colors = self._get_valid_colors(i, j)
                    if colors:
                        choices.append((i, j, colors))
        return choices

    def _get_valid_colors(self, i, j):
        if config.RULE_SET == 'classic':
            colors = config.CLASSIC_COLORS
            offsets = config.CLASSIC_OFFESTS
        elif config.RULE_SET_OPTIONS == 'modern':
            colors = config.MODERN_COLORS
            offsets = config.MODERN_OFFESTS
        return self._valid_colors(i, j, colors, offsets)

    def _valid_colors(self, i, j, colors, offsets):
        used_colors = set()
        for offset in offsets:
            x = i + offset[0]
            y = j + offset[1]
            if x >= 0 and x < len(self.field) and y >=0 and y < len(self.field):
                used_colors.add(self.field[x][y])
        used_colors.discard('O')
        return colors - used_colors
