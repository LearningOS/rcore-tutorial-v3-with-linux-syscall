import sys
import re


def test():
    output = sys.stdin.read(1000000)
    output = output.split('\n')
    count = 0
    for i in output:
        if re.search(r'test passed', i) or re.search(r'Pass', i):
            count += 1
    print("passed syscall ", count)

    assert count == 220

if __name__ == '__main__':
    test()

