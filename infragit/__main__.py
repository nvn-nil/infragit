import os
from subprocess import Popen, PIPE, STDOUT
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("command", nargs=1)
    parser.add_argument("--directory", "-d", type=str, required=False)

    args = parser.parse_args()

    command = args.command[0]
    directory = None
    if not args.directory:
        directory = os.getcwd()
    else:
        if os.path.isabs(args.directory):
            directory = os.path.abspath(args.directory)
        else:
            directory = os.path.abspath(os.path.join(os.getcwd(), args.directory))

    if command == "init":
        p = Popen(["terraform", "init"], stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=directory)
        p.wait()
        output = p.stdout.read().decode()

        if "The directory has no Terraform configuration files" in output:
            # print("The directory has no Terraform configuration files.")
            return 1
        
        print(output)

        os.makedirs(os.path.join(directory, ".igit"), exist_ok=True)
        return p.returncode

if __name__=="__main__":
    main()
