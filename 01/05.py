def main():
    s = 'I am an NLPer'
    ngram(2, s.split(' '))
    ngram(2, s.replace(' ', ''))


def ngram(n, w):
    r = []
    for i in range(len(w) - n + 1):
        r.append(w[i:i+n])
    print(r)

if __name__ == '__main__':
    main()
