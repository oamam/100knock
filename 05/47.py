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
    for chunks in parsed:
        for chunk in chunks.values():
            if chunk.has_pos('動詞') is False:
                continue
            verb_chunk = chunk
            verb_morph = verb_chunk.get_morph_by_pos('動詞')

            verb_sentence = ''
            particles = []
            particle_sentences = []

            for i in verb_chunk.dst:
                from_chunk = chunks[i]
                # サ変文節抽出
                if from_chunk.has_pos1('サ変接続') is True and \
                        from_chunk.has_surface('を') is True:
                    sahen_morph = from_chunk.get_morph_by_pos1('サ変接続')
                    wo_morph = from_chunk.get_morph_by_items(
                        {'pos': '助詞', 'surface': 'を'})
                    verb_sentence = sahen_morph.surface + \
                        wo_morph.surface + \
                        verb_morph.base + '\t'
                # 格助詞文節抽出
                elif from_chunk.has_items(
                        {'pos': '助詞', 'pos1': '格助詞'}) is True:
                    particle_chunk = from_chunk
                    particle_morph = particle_chunk.get_morph_by_items(
                        {'pos': '助詞', 'pos1': '格助詞'})
                    if particle_morph is None:
                        continue
                    particles.append(particle_morph.surface)
                    particle_sentences.append(particle_chunk.get_sentence())

            if len(verb_sentence) == 0 or \
                    len(particles) == 0 or \
                    len(particle_sentences) == 0:
                continue
            combined_particles = sorted(
                zip(particles, particle_sentences), key=lambda x: x[0])
            particles, particle_sentences = zip(*combined_particles)

            print('{}\t{}\t{}'.format(verb_sentence, ' '.join(
                particles), ' '.join(particle_sentences)))


def main():
    parsed = parse()
    extract_section(parsed)


if __name__ == '__main__':
    main()
