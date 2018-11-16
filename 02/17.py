import math


def main():
    lst = []
    with open('hightemp.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            lst.append(l.split("\t")[0])
    for s in set(lst):
        print(s)


if __name__ == '__main__':
    main()
