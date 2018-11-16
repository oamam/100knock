import gzip
import json
import re


def main():
    t = text()
    p = re.compile(
        r'^\{\{基礎情報.*?$(.*?)^\}\}$',
        re.MULTILINE + re.DOTALL
    )
    r = p.findall(t)
    pp = re.compile(
        r'^\|(.+?)\s*=\s*(.+)$',
        re.MULTILINE
    )
    rr = pp.findall(r[0])
    ppp = re.compile(
        r'(\'{2,5})(.*?)(\1)',
        re.MULTILINE
    )
    d = {}
    for l in rr:
        rrr = ppp.sub(r'\2', l[1])
        d[l[0]] = rrr
    print(d)


def text():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for l in f:
            j = json.loads(l)
            if j['title'] == 'イギリス':
                return j['text']


if __name__ == '__main__':
    main()
