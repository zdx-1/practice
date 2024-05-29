import sys
import os

read = sys.stdin.readline


def judge():
    n, m = list(map(int, input().split()))
    #    print(f'n={n},{m}')
    vis = [[0] * m for _ in range(m)]
    flag = True
    for idx in range(m):
        record = list(map(int, read().split()))
        money = 0
        for i in range(1, 2 * record[0] + 1, 2):
            if record[i] == -1:
                money = float('inf')
            else:
                if vis[record[i]][record[i + 1]] == 0:
                    flag = False
                else:
                    money += vis[record[i]][record[i + 1]]
                    vis[record[i]][record[i + 1]] = 0
        out = 2 * record[0] + 1
        for i in range(out + 2, len(record), 2):
            j = (i - out) // 2 - 1
            #            print(f'out={out},i={i},j={j}')
            vis[idx][j] = record[i]
            if money != float('inf'):
                money -= record[i]
        if money != float('inf') and money != 0:
            flag = False
    return 'YES' if flag == True else 'NO'


def main():
    t = int(input())
    for _ in range(t):
        print(judge())
    return


main()
