import argparse, os, sys

from . import data

def main():
    args = parse_args()
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')

    return parser.parse_args()


def init(args):
    try:
        data.init()
        print(f'Initialised empty repository in {os.getcwd()}/{data.GIT_DIR}.')
    except FileExistsError:
        print(f'Repository already initialised.')
    

def hash_object(args):
    with open(args.file, 'rb') as file:
        print(data.hash_object(file.read()))

def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object, expected=None))