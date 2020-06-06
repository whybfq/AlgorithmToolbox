
import sys


def get_majority_element(seq, l, r):
    if l + 1 == r or l + 2 == r:
        return seq[ l ]
    m = (l + r) // 2
    left = get_majority_element(seq, l, m)
    right = get_majority_element(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[ l:r ]:
        if i == left:
            c1 += 1
        elif i == right:
            c2 += 1
    if c1 > (r - l) // 2 and left != -1:
        return left
    elif c2 > (r - l) // 2 and right != -1:
        return right
    else:
        return -1


if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    print(int(get_majority_element(a, 0, n) != -1))
