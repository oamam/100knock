import MeCab


def main():
    parsed = analysis()
    surfaces = ''
    c = 0
    nouns = []
    for row in parsed:
        if row['pos'] == '名詞':
            surfaces += row['surface']
            c += 1
        elif c > 1:
            nouns.append(surfaces)
            surfaces = ''
            c = 0
        else:
            surfaces = ''
            c = 0
    if c > 0:
        nouns.append(surfaces)
    print(len(set(nouns)))


def analysis():
    mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')
    result = []
    with open('neko.txt') as input_data:
        for line in input_data:
            pdata = mecab.parse(line)
            for pline in pdata.split('\n'):
                if pline.count('\t') == 0:
                    continue
                surface, estimated = pline.split('\t')
                items = estimated.split(',')
                result.append({
                    'surface': surface,
                    'base': items[6],
                    'pos': items[0],
                    'pos1': items[1]
                })
    return result


if __name__ == '__main__':
    main()
