"""
Regex postprocess rst output
"""
import sys
import re

hat = """
Python API
==========
_
++++++++++
_
??????????
_
~~~~~~~~~~

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
        lambda m: '\n\n======\n\n{} (*{}*)\n------\n'.format(m.group(1), m.group(2).replace('*', '\\*')),
        text
    )


def attr_rep(text):
    return re.sub(r'\n(.*?) : (.*?)\r?\n',  # [^\S\r\n]+
                  lambda m: '\n{} (*{}*)\n------\n'.format(m.group(1), m.group(2).replace('*', '\\*')),  # '    '
                  text)

def rep(text):
    # fix parameters tables on GitHub:
    text = text.replace('\n         * ', '\n          * ')
    # make broken bold lines whole again:
    text = join_lines(join_lines(text, 0), 3)
    # bold lines to left plus ==== underline:
    text = to_header(to_header(text, 0), 3)
    # remove 2nd quotes:
    text = text.replace('\n   ', '\n')
    # before and after 2nd ====:
    m = re.search(r'(.*?\n===[=]+\r?\n.*?\n===[=]+\r?\n)(.*)', text, re.DOTALL)
    text = attr_rep(m.group(1)) + m.group(2)
    #
    text = text.replace('class shortcutter.base', 'class shortcutter')
    return hat + text

def main():
    sys.stdout.write(rep(sys.stdin.read()))


if __name__ == '__main__':
    main()
