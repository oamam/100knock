import random


def main():
    negs = read_file('rt-polaritydata/rt-polarity.neg')
    poss = read_file('rt-polaritydata/rt-polarity.pos')
    sentiments = []
    sentiments.extend(add_prefix(negs, '-1'))
    sentiments.extend(add_prefix(poss, '+1'))
    random.shuffle(sentiments)
    write_file(sentiments)


def read_file(path):
    with open(path, encoding='cp1252') as f:
        return f.readlines()


def write_file(sentiments):
    with open('sentiments.txt', mode='w') as f:
        for s in sentiments:
            f.write(s)


def add_prefix(lines, p):
    res = []
    for line in lines:
        res.append(p + line)
    return res


if __name__ == '__main__':
    main()
