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
    indentation = ''.join([' ' for i in range(indent)])
    return re.sub(
        r'\r?\n{dent}\*\*([^\*\n]+[^\n]*)\*\*\r?\n'.format(dent=indentation),
        lambda m: '\n{}\n{}\n'.format(m.group(1), ''.join([header for i in range(len(m.group(1)))])),
        text
    )


def rep(text):
    text = text.replace('\n         * ', '\n          * ').replace('class shortcutter.base', 'class shortcutter')
    text = join_lines(join_lines(text, 0), 3)
    text = to_header(to_header(text, 0, '='), 3, '-')
    text = text.replace('\n   ', '\n')
    m = re.search(r'(.*?\n---[-]+\r?\n)(.*)', text, re.DOTALL)
    text = m.group(1) + m.group(2).replace('\n   ', '\n')
    return text

def main():
    sys.stdout.write(rep(sys.stdin.read()))


if __name__ == '__main__':
    main()
