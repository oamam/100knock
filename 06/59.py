from xml.etree import ElementTree


def main():
    tree = ElementTree.parse('nlp.txt.xml')
    root = tree.getroot()
    document = root[0]
    sentences = document[1]

    for sentence in sentences:
        s_f = sentence[1].text
        extract(s_f)


def extract(f):
    key = '(NP'
    kl = len(key)
    oi = f.find(key)
    while oi >= 0:
        ci = oi + kl
        c = 1
        for s in f[oi+kl:]:
            ci += 1
            if s == ')':
                c -= 1
                if c == 0:
                    break
            if s == '(':
                c += 1
        words = []
        for s in f[oi:ci+1].split(' '):
            if ')' in s:
                word = s.replace(')', '')
                words.append(word)
        print(' '.join(words))
        oi = f.find('(NP', oi + kl)


if __name__ == '__main__':
    main()
