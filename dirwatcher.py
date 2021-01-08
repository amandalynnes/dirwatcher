#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Amanda Simmons"

import sys
import time
import os


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    # Your code here
    return


def signal_handler(sig_num, frame):
    # Your code here
    return


def main(args):
    while True:
        print(f'my PID is: {os.getpid()} ')
        time.sleep(1)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
