import gzip
import json
import re


def main():
    t = text()
    p = re.compile(
        r'^(\={2,})\s*(.+?)\s*\1.*$',
        re.MULTILINE
    )
    r = p.findall(t)
    for l in r:
        lv = (len(l[0]) - 1)
        print('{}{}({})'.format('\t'*(lv - 1), l[1], lv))


def text():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for l in f:
            j = json.loads(l)
            if j['title'] == 'イギリス':
                return j['text']


if __name__ == '__main__':
    main()
