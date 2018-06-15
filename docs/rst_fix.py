"""
Regex postprocess rst output
"""
import sys
import re


def join_lines(text: str, indent: int):
    indentation = ''.join([' ' for i in range(indent)])
    return re.sub(
        r'\r?(\n{dent}\*\*[^\r\n]+)\r?\n{dent}([^\s\r\n][^\r\n]*\*\*\r?\n)'.format(dent=indentation),
        lambda m: '{} {}'.format(m.group(1), m.group(2)),
        text
    )


def to_header(text: str, indent: int, header: str):
    """
    ``********`` denotes top header
    """
    indentation = ''.join([' ' for i in range(indent)])
    return re.sub(
        r'\r?\n{dent}\*\*([^\*\n]+[^\n]*)\*\*\r?\n'.format(dent=indentation),
        lambda m: '\n{}\n{}\n\n{}\n'.format(m.group(1),
                                            ''.join([header for i in range(len(m.group(1)))]),
                                            '********'),
        text
    )


def rep(text):
    # fix parameters tables on GitHub:
    text = text.replace('\n         * ', '\n          * ')
    #
    text = text.replace('class shortcutter.base', 'class shortcutter')
    # make broken bold lines whole again:
    text = join_lines(join_lines(text, 0), 3)
    # bold lines to ---- header plus **** underline:
    text = to_header(to_header(text, 0, '-'), 3, '-')
    # remove quotes before second ----:
    text = text.replace('\n   ', '\n')
    # remove quotes after second ----:
    m = re.search(r'(.*?\n---[-]+\r?\n.*?\n---[-]+\r?\n)(.*)', text, re.DOTALL)
    text = m.group(1) + m.group(2).replace('\n   ', '\n')
    #
    return text

def main():
    sys.stdout.write(rep(sys.stdin.read()))


if __name__ == '__main__':
    main()
