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


def extract_section(parsed):
    for chunks in parsed[:10]:
        trees = []
        for chunk in chunks.values():
            tree = []
            if chunk.has_pos('名詞') is False:
                continue
            if 0 > chunk.srcs:
                continue
            tree.append(chunk)
            srcs = chunk.srcs
            while True:
                next_chunk = chunks[srcs]
                tree.append(next_chunk)
                if 0 > next_chunk.srcs:
                    break
                srcs = next_chunk.srcs
            if len(tree) > 0:
                trees.append(tree)
        for i in range(len(trees)):
            x_tree = trees[i][::]
            x = x_tree.pop(0)
            for ii in range(i + 1, len(trees)):
                y_tree = trees[ii][::]

                last_trees = []
                xi = 0
                while len(x_tree) > xi:
                    yi = 0
                    ystart = 0
                    xstart = 0
                    while len(y_tree) > yi:
                        if x_tree[xi].get_sentence() != \
                                y_tree[yi].get_sentence():
                            yi += 1
                            continue
                        xstart = xi
                        ystart = yi
                        while True:
                            if xi >= len(x_tree) or yi >= len(y_tree):
                                break
                            if x_tree[xi].get_sentence() != \
                                    y_tree[yi].get_sentence():
                                break
                            last_trees.append(x_tree[xi])
                            xi += 1
                            yi += 1
                        break
                    xi += 1

                if len(y_tree[:ystart]) == 0:
                    common_trees = y_tree[ystart:]
                else:
                    common_trees = y_tree[:ystart]

                outputs = []
                outputs.append(x.get_tree_sentence('X'))

                x_sentences = [xt.get_sentence() for xt in x_tree[:xstart]]
                if 1 > len(x_sentences):
                    outputs.append(' | ')
                else:
                    outputs.append(' -> ' + ' -> '.join(x_sentences) + ' -> ')

                if [ct.get_sentence() for ct in common_trees] == \
                        [lt.get_sentence() for lt in last_trees]:
                    outputs.append('Y')
                else:
                    outputs.append(y_tree[0].get_tree_sentence('Y'))
                    if len(common_trees[1:]) > 0:
                        outputs.append(' -> ' + ' -> '.join(
                            [ct.get_sentence()for ct in common_trees[1:]]))
                    outputs.append(' | ' + last_trees[0].get_sentence())

                print(''.join(outputs))


def main():
    parsed = parse()
    extract_section(parsed)


if __name__ == '__main__':
    main()
