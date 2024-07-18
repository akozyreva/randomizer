import random
from argparse import ArgumentParser


def _get_command_line_options() -> tuple[int, int]:
    parser = ArgumentParser(description='Enter nums for random')
    parser.add_argument('--num1', '-n1', help="Specify 1 num", required=True, type=int)
    parser.add_argument('--num2', '-n2', help="Specify 2 num", required=True, type=int)
    options = parser.parse_args()
    num1, num2 = vars(options).values()
    return num1, num2


if __name__ == '__main__':
    num1, num2 = _get_command_line_options()
    random_number = random.randint(num1, num2)
    print()
    print(random_number)