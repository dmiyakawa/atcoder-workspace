#!/usr/bin/env python3

import pyperclip

def main():
    s = pyperclip.paste().rstrip()
    print(s)


if __name__ == "__main__":
    main()
