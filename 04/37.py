import MeCab
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():
    parsed = analysis()
    dcounts = {}
    for row in parsed:
        if row['surface'] in dcounts:
            dcounts[row['surface']] += 1
        else:
            dcounts[row['surface']] = 1
    sorted_dcounts = sorted(dcounts.items(), key=lambda x: -x[1])
    x, y = list(zip(*sorted_dcounts[:10]))
    mpl.rcParams['font.family'] = 'AppleGothic'
    plt.bar(x, y)
    plt.show()


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
