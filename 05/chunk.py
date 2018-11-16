class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst = []
        self.srcs = 0

    def __str__(self):
        return '<morphs: {}, dst: {}, srcs: {}>'.format(
            self.morphs, self.dst, self.srcs
        )

    def delete_mark_morphs(self):
        for i, morph in enumerate(self.morphs):
            if morph.surface in ['、', '。', '」']:
                del self.morphs[i]

    def has_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def has_pos1(self, pos1):
        for morph in self.morphs:
            if morph.pos1 == pos1:
                return True
        return False

    def has_surface(self, surface):
        for morph in self.morphs:
            if morph.surface == surface:
                return True
        return False

    def has_items(self, items):
        for morph in self.morphs:
            if all([getattr(morph, k) == v for k, v in items.items()]) is True:
                return True
        return False

    def get_morph_by_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return morph
        return None

    def get_morph_by_pos1(self, pos1):
        for morph in self.morphs:
            if morph.pos1 == pos1:
                return morph
        return None

    def get_morph_by_items(self, items):
        for morph in self.morphs:
            if all([getattr(morph, k) == v for k, v in items.items()]):
                return morph
        return None

    def get_sentence(self):
        self.delete_mark_morphs()
        return ''.join([morph.surface for morph in self.morphs])

    def get_tree_sentence(self, r):
        if 1 > len(self.morphs):
            return ''
        self.delete_mark_morphs()
        if self.morphs[0].pos == '名詞':
            return r + ''.join([morph.surface for morph in self.morphs[1:]])
        return ''
