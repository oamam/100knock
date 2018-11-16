import math


def main():
    with open('hightemp.txt', 'r') as f:
        lines = f.readlines()
        lst = []
        for l in lines:
            lst.append(l.split("\t")[0])
        set_lst = set(lst)
        dt = {}
        for s in set_lst:
            dt[s] = lst.count(s)
        dt = sorted(dt.items(), key=lambda x: x[1], reverse=True)
        for s, c in dt:
            print('{}({})'.format(s, c))


if __name__ == '__main__':
    main()
