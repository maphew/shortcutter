"""
Regex postprocess rst output
"""
import sys
import re

hat = """
Python API
==========
_
++++++
_
??????

ShortCutter
~~~~~~~~~~~

"""


def join_lines(text: str, indent: int):
    indentation = ''.join([' ' for i in range(indent)])
    return re.sub(
        r'((?:\n|^){dent}\*\*[^\r\n]+)\r?\n{dent}([^\s\r\n][^\r\n]*\*\*\r?\n)'.format(dent=indentation),
        lambda m: '{} {}'.format(m.group(1), m.group(2)),
        text
    )


def to_header(text: str, indent: int):
    """
    ``======`` denotes top header
    ``------`` denotes smallest header
    """
    indentation = ''.join([' ' for i in range(indent)])
    return re.sub(
        r'(?:\n|^){dent}\*\*([^\*\n\(\)]+[^\n\(\)]*)\(([^\n]*?)\)\*\*\r?\n'.format(dent=indentation),
        lambda m: '\n\n======\n\n``{}`` (*{}*)\n------\n'.format(m.group(1), m.group(2).replace('*', '\\*')),
        text
    )


def attr_rep(text):
    return re.sub(r'\n(.*?) : (.*?)\r?\n',  # [^\S\r\n]+
                  lambda m: '\n{} (*{}*)\n------\n'.format(m.group(1), m.group(2).replace('*', '\\*')),  # '    '
                  text)

def rep(text):
    # fix parameters tables on GitHub:
    text = text.replace('\n         * ', '\n          * ')
    #
    text = text.replace('class shortcutter.base', 'class shortcutter')
    # make broken bold lines whole again:
    text = join_lines(join_lines(text, 0), 3)
    # bold lines to left plus ==== underline:
    text = to_header(to_header(text, 0), 3)
    # remove quotes before and after 2nd ====:
    m = re.search(r'(.*?\n===[=]+\r?\n.*?\n===[=]+\r?\n)(.*)', text, re.DOTALL)
    text = attr_rep(m.group(1).replace('\n   ', '\n')) + m.group(2).replace('\n      ', '\n')
    #
    return hat + text

def main():
    sys.stdout.write(rep(sys.stdin.read()))


if __name__ == '__main__':
    main()
