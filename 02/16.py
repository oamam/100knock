import math


def main():
    n = int(input('N: '))
    with open('hightemp.txt', 'r') as f:
        lines = f.readlines()
        ln = len(lines)
        it = math.ceil(ln / n)
        for i in range(0, ln, it):
            print('---')
            for l in lines[i:i+it]:
                print(l.rstrip())


if __name__ == '__main__':
    main()
