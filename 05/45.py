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
        for chunk in chunks.values():
            if chunk.has_pos('動詞') is False:
                continue
            verb_chunk = chunk

            verb_sentence = verb_chunk.get_morph_by_pos('動詞').base
            particles = []

            for i in verb_chunk.dst:
                from_chunk = chunks[i]
                # 格助詞文節抽出
                if from_chunk.has_items(
                        {'pos': '助詞', 'pos1': '格助詞'}) is True:
                    particle_chunk = from_chunk
                    particle_morph = particle_chunk.get_morph_by_items(
                        {'pos': '助詞', 'pos1': '格助詞'})
                    if particle_morph is None:
                        continue
                    particles.append(particle_morph.surface)

            if len(verb_sentence) == 0 or \
                    len(particles) == 0:
                continue
            particles.sort()
            print('{}\t{}'.format(verb_sentence, ' '.join(particles)))


def main():
    parsed = parse()
    extract_section(parsed)


if __name__ == '__main__':
    main()
