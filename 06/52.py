import re
from nltk import stem


def main():
    stemmer = stem.PorterStemmer()
    with open('nlp.txt') as f:
        p = re.compile(
            r'(^.*?[\.|;|:|\?|!])\s([A-Z].*)',
            re.MULTILINE + re.DOTALL
        )
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            while True:
                matched = p.match(line)
                if matched:
                    for w in matched.group(1).split(' '):
                        print('{}\t{}'.format(
                            w.replace('.', ''),
                            stemmer.stem(w.replace('.', ''))
                        ))
                    print('')
                    line = matched.group(2)
                else:
                    break


if __name__ == '__main__':
    main()
