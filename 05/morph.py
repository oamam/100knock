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

    def __eq__(self, other):
        return self.surface == other.surface and \
            self.base == other.base and \
            self.pos == other.pos and \
            self.pos1 == other.pos1
