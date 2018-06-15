import sys
import re

def rep(text):
    text = text.replace('\n         * ', '\n          * ')
    # text = re.sub(
    #     r'((?<=[^\\]ˎ)|(?<=^ˎ))[^ˎ]*(?=ˎ)',
    #     lambda m: sugartex.replace(m.group(0)),
    #     text
    # )
    return text

def main():
    sys.stdout.write(rep(sys.stdin.read()))


if __name__ == '__main__':
    main()
