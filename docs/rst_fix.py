"""
Regex postprocess rst output
"""
import sys
import re

hat = """
Python API
==========

ShortCutter
-----------

"""


def join_lines(text: str, indent: int):
    indentation = ''.join([' ' for i in range(indent)])
    return re.sub(
        r'\r?(\n{dent}\*\*[^\r\n]+)\r?\n{dent}([^\s\r\n][^\r\n]*\*\*\r?\n)'.format(dent=indentation),
        lambda m: '{} {}'.format(m.group(1), m.group(2)),
        text
    )


def to_header(text: str, indent: int, header: str):
    """
    ``========`` denotes top header
    """
    indentation = ''.join([' ' for i in range(indent)])
    return re.sub(
        r'\r?\n{dent}\*\*([^\*\n\(\)]+[^\n\(\)]*)\(([^\n]*?)\)\*\*\r?\n'.format(dent=indentation),
        lambda m: '\n\n{}\n\n**{}** (*{}*)\n'.format('========', m.group(1), m.group(2)),
        text
    )


def rep(text):
    # fix parameters tables on GitHub:
    text = text.replace('\n         * ', '\n          * ')
    #
    text = text.replace('class shortcutter.base', 'class shortcutter')
    # make broken bold lines whole again:
    text = join_lines(join_lines(text, 0), 3)
    # bold lines to left plus ==== underline:
    text = to_header(to_header(text, 0, '-'), 3, '-')
    # remove quotes before third ====:
    text = text.replace('\n   ', '\n')
    # remove quotes after third ====:
    block = r'.*?\n===[=]+\r?\n'
    m = re.search(r'({b}{b}{b})(.*)'.format(b=block), text, re.DOTALL)
    text = m.group(1) + m.group(2).replace('\n   ', '\n')
    #
    return hat + text

def main():
    sys.stdout.write(rep(sys.stdin.read()))


if __name__ == '__main__':
    main()
