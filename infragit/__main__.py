from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("command", nargs=1)

    args = parser.parse_args()
    print(args.command)


if __name__=="__main__":
    main()
