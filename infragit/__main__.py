import os
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("command", nargs=1)
    parser.add_argument("--directory", "-d", type=str, required=False)

    args = parser.parse_args()

    command = args.command[0]
    directory = os.getcwd() if not args.directory else os.path.abspath(os.path.join(os.getcwd(), args.directory))

    if command == "init":
        print("Creating folder:", os.path.join(directory, ".igit"))
        os.makedirs(os.path.join(directory, ".igit"), exist_ok=True)


if __name__=="__main__":
    main()
