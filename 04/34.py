import MeCab


def main():
    parsed = analysis()
    for i, row in enumerate(parsed):
        if row['surface'] == 'の' \
                and row['pos'] == '助詞' \
                and parsed[i-1]['pos'] == '名詞' \
                and parsed[i+1]['pos'] == '名詞':
            print('{}{}{}'.format(
                parsed[i-1]['surface'],
                row['surface'],
                parsed[i+1]['surface']
            ))


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
