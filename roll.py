#!python3
import getopt
from random import randrange
import sys


def roll_die(sides: int = 6) -> int:
    return randrange(0, sides) + 1


def roll_multiple(number: int, sides: int = 6):
    for roll_number in range(0, number):
        roll = roll_die(sides)
        print(f"roll number {roll_number}: {roll}")

def roll_interactive(sides: int = 6):
    roll_number = 1
    should_roll = True
    while should_roll:
        roll = roll_die(sides)
        print(f"roll number {roll_number} of a {sides} sided die: {roll}")
        should_roll = roll_again()
        roll_number += 1


def roll_again():
    should_check = True
    while should_check:
        cont = input("roll again? (y/n): ")
        try:
            cont = cont.upper()
        except (ValueError, TypeError):
            should_check = True
        else:
            if cont == 'Y':
                return True
            elif cont == 'N':
                return False

def get_args(args):
    opts, args = getopt.getopt(args, "hn:s:",["help"])
    # print((opts, args))
    return (opts, args)

def cli(args):
    opts, args = get_args(args)
    sides = 6
    interactive = True
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_text)
            exit()
        elif opt == '-s':
            sides = int(arg)
        elif opt == "-n":
            interactive = False
            number = int(arg)
    if interactive:
        roll_interactive(sides)
    if not interactive:
        roll_multiple(number,sides)

help_text = """
This program is a die roller
-s option sets the number of sides (not bound by the physical realm)
-n option sets the number of rolls (default 6)
-h or --help prints this text

if run without -n interactive mode is entered
"""
if __name__ == '__main__':
    cli(sys.argv[1:])
