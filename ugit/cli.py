import argparse, os

from .data import init as hidden, GIT_DIR

def main():
    args = parse_args()
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    return parser.parse_args()

def init(args):
    try:
        hidden()
        print(f'Initialised empty repository in {os.getcwd()}/{GIT_DIR}.')
    except FileExistsError:
        print(f'Repository already initialised.')