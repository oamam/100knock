import gzip
import json
import re


def main():
    t = text()
    p = re.compile(
        r'(?:File|ファイル):(.+?)\|',
        re.MULTILINE
    )
    r = p.findall(t)
    for l in r:
        print(l)


def text():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for l in f:
            j = json.loads(l)
            if j['title'] == 'イギリス':
                return j['text']


if __name__ == '__main__':
    main()
