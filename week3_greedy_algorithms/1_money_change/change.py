# Uses python3
import sys


def get_change(money):
    return int(money/10) + int(money % 10 / 5) + money % 5
    # numCoinns = 0
    # while money > 0:
    #     if money > 10:
    #         money -= 10
    #     elif money > 5:
    #         money -= 5
    #     else:
    #         money -= 1
    #     numCoinns += 1
    # return numCoinns


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
