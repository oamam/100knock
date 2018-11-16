import gzip
import json
import re
import copy


def main():
    t = text()
    a = base(t)
    b = copy.deepcopy(a)
    for sy in [
        r'\[\[((?!ファイル|File|Category)[^|]*?)\]\]',
        r'\[\[(?:(?!ファイル|File|Category).*?)\|(.*?)\]\]'
    ]:
        p = re.compile(sy, re.MULTILINE)
        for k, v in b.items():
            r = p.sub(r'\1', v)
            b[k] = r
    for k, v in b.items():
        print('{}:\n\t前:{}\n\t後:{}'.format(k, a[k], v))


def base(t):
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
    d = {}
    for l in rr:
        d[l[0]] = l[1]
    return d


def text():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for l in f:
            j = json.loads(l)
            if j['title'] == 'イギリス':
                return j['text']


if __name__ == '__main__':
    main()
