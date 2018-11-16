import math


def main():
    with open('hightemp.txt', 'r') as f:
        lines = f.readlines()
        lines.sort(key=lambda l: float(l.split("\t")[2]), reverse=True)
    for l in lines:
        print(l.rstrip())


if __name__ == '__main__':
    main()
