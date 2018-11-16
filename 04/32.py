import MeCab


def main():
    parsed = analysis()
    for row in parsed:
        if row['pos'] == '動詞':
            print(row['base'])


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
