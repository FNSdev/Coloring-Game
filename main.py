import argparse

import config
from core import ColoringGame

def parse_args(args):
    for k, v in args.items():
        if k == 'size':
            l = config.MIN_FIELD_SIZE
            r = config.MAX_FIELD_SIZE
            if l <= v <= r:
                config.FIELD_SIZE = v
            else:
                raise ValueError(f'Field size should be in range [{l}, {r}]')
        elif k == 'rules':
            if v in config.RULE_SET_OPTIONS:
                config.RULE_SET = v
            else:
                raise ValueError(f'Available rule sets: {config.RULE_SET_OPTIONS}')
        elif k == 'enemy':
            if v in config.PLAY_AGAINST_OPTIONS:
                config.PLAY_AGAINST = v
            else:
                raise ValueError(f'Available play against options: {config.PLAY_AGAINST_OPTIONS}')


def main():
    parser = argparse.ArgumentParser(description='Specify game settings')
    parser.add_argument(
        '--size',
        type=int,
        help=f'select field size in range [{config.MIN_FIELD_SIZE}, {config.MAX_FIELD_SIZE}]', 
        default=config.FIELD_SIZE)
    parser.add_argument(
        '--rules', 
        type=str, 
        help=f'select rule set: {config.RULE_SET_OPTIONS}', 
        default=config.RULE_SET)
    parser.add_argument(
        '--enemy', 
        type=str, 
        help=f'select enemy: {config.PLAY_AGAINST_OPTIONS}', 
        default=config.PLAY_AGAINST)


    args = vars(parser.parse_args())
    parse_args(args)

    game = ColoringGame()
    game.start()

if __name__ == "__main__":
    main()