#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Amanda Simmons, Piero Mader, Pete Mayor, Alec Stephens"

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

exit_flag = False
logger = logging.getLogger(__name__)
logging.basicConfig(
    # filename='search_results.log',
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG,)

txt_dict = {}


def search_for_magic(filename, start_line, magic_string):
    """ Searches for text arg in files, picking up where it left off. """
    with open(filename) as f:
        index = -1
        for index, line in enumerate(f):
            if index >= start_line:
                if magic_string in line:
                    logger.info(f'"{magic_string}" found on line {index+1}')
        # moves the bookmark whether string found or not
        txt_dict[filename] = index + 1


def watch_directory(path, magic_string, extension):
    """ Monitors files in the specified directory that end
    in the specified extension for any changes.  """
    # look at the files in the provided directory that end in the extension
    # and see which line in the file has the specified text

    files_in_dir = [path + '/' + f for f in os.listdir(path)]
    # this is where I am removing files from my watch list
    for k in list(txt_dict):
        if k not in files_in_dir:
            del txt_dict[k]
            logger.info(f'{k} file DELETED')
    # this is where I am adding files to my watch list
    for f in files_in_dir:
        if f.endswith(extension):
            if f not in txt_dict:
                txt_dict[f] = 0
                logger.info(f'{f} file ADDED')
    for f in txt_dict:
        # change this to use os.path.join to work with every os
        search_for_magic(f, txt_dict[f], magic_string)


def create_parser():
    """Creates an instance of the parser object."""
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='directory to watch for')
    parser.add_argument('text', help='magic_string text to search for')
    parser.add_argument(
        '--extension', help='required file extension', default='.txt')
    parser.add_argument(
        '--interval', help='polling interval', type=int, default=1)

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
    global exit_flag
    # log the associated signal name
    logger.warning('Received ' + signal.Signals(sig_num).name)

    exit_flag = True
    if exit_flag:
        logger.info(f'Stopped process: {os.getpid()}')
    return


def main(args):
    """ Runs parser, runs watch directory function and
    catches any exceptions """

    logger.info(f'Started process: {os.getpid()}')
    parser = create_parser()

    parsed_args = parser.parse_args(args)
    polling_interval = parsed_args.interval
    directory = parsed_args.directory
    text = parsed_args.text
    extension = parsed_args.extension

    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.

    while not exit_flag:
        try:
            # call my directory watching function
            watch_directory(directory, text, extension)

        except OSError as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            logger.error(e)

        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            logger.error(e)

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start

    return


if __name__ == '__main__':
    main(sys.argv[1:])
