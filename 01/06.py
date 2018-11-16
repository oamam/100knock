def main():
    a = ngram(2, 'paraparaparadise')
    b = ngram(2, 'paragraph')
    print('和集合：{}'.format(set(a) | set(b)))
    print('積集合：{}'.format(set(a) & set(b)))
    print('差集合：{}'.format(set(a) - set(b)))
    print('does paraparaparadise have se ? {}'.format('se' in a))
    print('does paragraph have se ? {}'.format('se' in b))


def ngram(n, w):
    r = []
    for i in range(len(w) - n + 1):
        r.append(w[i:i+n])
    return r

if __name__ == '__main__':
    main()
