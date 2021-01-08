#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Amanda Simmons, Piero Mader, Pete Mayor"

import sys
import time
import os
import argparse
import signal
import logging

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
    """Creates an argument parser object."""
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='magic_string text to search for')
    parser.add_argument('dir', help='directory to watch for')
    parser.add_argument('extension', help='required file extension')
    parser.add_argument('interval', help='polling interval', type=int)

    return parser


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT.
    Other signals can be mapped here as well (SIGHUP?)
    Basically, it just sets a global flag,
    and main() will exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    logger = logging.getLogger(__name__)
    # https://realpython.com/python-logging/
    f_handler = logging.FileHandler('file.log')
    f_handler.setLevel(logging.warning)
    f_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    # log the associated signal name
    logger.warning('Received ' + signal.Signals(sig_num).name)
    return


def main(args):
    """ """
    print(f'my PID is: {os.getpid()} ')
    parser = create_parser()

    parsed_args = parser.parse_args(args)
    polling_interval = parsed_args.interval

    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.

    exit_flag = False
    while not exit_flag:
        try:
            # call my directory watching function
            print('hello')
        except Exception as e:
            global exit_flag
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            print(e)
            exit_flag = True

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start

    return


if __name__ == '__main__':
    main(sys.argv[1:])
