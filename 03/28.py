import gzip
import json
import re
import copy


def main():
    t = text()
    a = base(t)
    a['補足1'] = '[[Category: あいうえお[[かきくけこ]]]]'
    a['補足2'] = '#REDIRECT [[あいうえお#かきくけこ]]'
    a['補足3'] = '~~~~'
    a['補足4'] = '<!-- コメントアウトしたいテキスト -->'
    a['補足5'] = '* いち\n* に\n** に の いち\n* さん'
    a['補足6'] = '; いち\n: いちの説明\n; に\n: にの説明'
    b = copy.deepcopy(a)
    for sy in [
        r'(?:\'{2,5})(.+?)(?:\'{2,5})',
        r'\[\[(?:File|ファイル):(.*?)\|.*\]\]',
        r'\[\[Category:(.*?)(?:\|.*)?\]\]',
        r'.*\#REDIRECT\s*\[\[(.*?)\]\]',
        r'\[\[([^|]*?)\]\]',
        r'\[\[(?:.*?)\|(.*?)\]\]',
        r'\[(?:http.*?)\s(.*?)\]',
        r'\[(http[^\s]*?)\]',
        r'~{4,}(.*)',
        r'\<\!\-\-\s(.*?)\s\-\-\>',
        r'^(?:\={2,})\s*(.+?)\s*(?:\={2,})',
        r'^(?:[\*\#]{1,})(.+?)',
        r'^(?:[\;\:])(.+?)',
        r'^-{3,}(.*)',
        r'\{\{(.*?)\}\}'
    ]:
        p = re.compile(sy, re.MULTILINE + re.DOTALL)
        for k, v in b.items():
            r = p.sub(r'\1', v)
            b[k] = r
    for k, v in b.items():
        print('{}:\n\t前:{}\n\t後:{}'.format(
            k, a[k].replace('\n', '\\n'), v.replace('\n', '\\n')
        ))


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
