#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Amanda Simmons"

import sys
import time
import os

# Success Criteria
# Use all best practices that have been taught so far: docstrings, PEP8,
# clean and readable code, and meaningful commit messages
# Have a demonstrable OS signal handler
# Log messages for files containing "magic text"
# Handle and log different exceptions such as "file not found",
# "directory does not exist", as well as handle and report
# top-level unknown exceptions so that your program stays alive
# Include a startup and shutdown banner in your logs and report
# the total runtime (uptime) within your shutdown log banner
# (please see the hints below if you don't understand what a logging banner is)
# Read the rubric!


def search_for_magic(filename, start_line, magic_string):
    """ """

    return


def watch_directory(path, magic_string, extension, interval):
    """ """

    return


def create_parser():
    # """Creates an argument parser object."""
    # parser = argparse.ArgumentParser()
    # parser.add_argument('', help='')
    # parser.add_argument('', help=')

    # return parser
    return


def signal_handler(sig_num, frame):
    """ """

    return


def main(args):
    """ """
    print(f'my PID is: {os.getpid()} ')
    while True:
        print('tick')
        time.sleep(2)
        print('tock')
        time.sleep(2)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
