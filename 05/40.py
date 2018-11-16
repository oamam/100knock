import CaboCha


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '<surface: {}, base: {}, pos: {}, pos1: {}>'.format(
            self.surface, self.base, self.pos, self.pos1
        )


def main():
    cabocha = CaboCha.Parser()
    morphs = []
    with open('neko.txt') as input_data:
        for line in input_data:
            parsed = cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
            for row_result in parsed.split('\n'):
                if row_result == '':
                    continue
                if row_result[0] == '*':
                    continue
                if row_result == 'EOS':
                    continue
                surface, right = row_result.split('\t')
                items = right.split(',')
                morphs.append(Morph(surface, items[6], items[0], items[1]))
    for morph in morphs:
        print(morph)


if __name__ == '__main__':
    main()
