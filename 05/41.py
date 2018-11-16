import CaboCha
from morph import Morph
from chunk import Chunk


def parse():
    cabocha = CaboCha.Parser()
    result = []
    with open('neko.txt') as input_data:
        for line in input_data:
            line = line.strip()
            parsed = cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
            chunks = {}
            for sentence_str in parsed.split('* '):
                sentence_analysis = sentence_str.split('\n')
                affliation_str = sentence_analysis.pop(0)
                if affliation_str in ['', 'EOS']:
                    continue
                morph_analysis = affliation_str.split(' ')
                chunk = Chunk()
                chunk.id = int(morph_analysis[0])
                chunk.srcs = int(morph_analysis[1][:-1])
                morphs = []
                for morph_str in sentence_analysis:
                    if morph_str in ['', 'EOS']:
                        continue
                    surface, right = morph_str.split('\t')
                    morph_items = right.split(',')
                    morphs.append(Morph(surface, morph_items[6],
                                        morph_items[0], morph_items[1]))
                chunk.morphs = morphs
                chunks[chunk.id] = chunk
            for i, chunk in chunks.items():
                if chunk.srcs > 0:
                    chunks[chunk.srcs].dst.append(i)
            result.append(chunks)
    return result


def main():
    parsed = parse()
    for i, chunk in parsed[7].items():
        sentence = ''
        for morph in chunk.morphs:
            sentence += morph.surface
        print('[{}]{} dst:{} srcs:{}'.format(i, sentence,
                                             chunk.dst, chunk.srcs))


if __name__ == '__main__':
    main()
