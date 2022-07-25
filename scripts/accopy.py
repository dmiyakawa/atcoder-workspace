#!/usr/bin/env python3
import argparse
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

import pyperclip

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", default="main.py")
    parser.add_argument("-d", "--debug", action="store_true", help="Turn on debugging logs")
    args = parser.parse_args()
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setFormatter(Formatter("%(levelname)s %(message)s"))
    logger.addHandler(handler)
    if args.debug:
        logger.setLevel(DEBUG)
    else:
        logger.setLevel(INFO)

    with open(args.filename) as f:
        pyperclip.copy(text=f.read())


if __name__ == "__main__":
    main()
