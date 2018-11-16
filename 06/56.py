from xml.etree import ElementTree


def main():
    tree = ElementTree.parse('nlp.txt.xml')
    root = tree.getroot()
    document = root[0]
    sentences = document[1]
    coreferences = document[2]
    replaces = {}
    for coreference in coreferences:
        for mention in coreference[1:]:
            sentence_index = int(mention[0].text)
            if sentence_index not in replaces:
                replaces[sentence_index] = []
            replaces[sentence_index].append(
                [
                    int(mention[1].text),
                    int(mention[2].text),
                    mention[4].text,
                    coreference[0][4].text
                ]
            )

    replaced_sentences = []
    for sentence in sentences:
        sentence_id = int(sentence.attrib['id'])
        tokens = sentence[0]
        sentence_str = ' '.join([token[0].text for token in tokens])
        if sentence_id in replaces:
            for row in replaces[sentence_id]:
                sentence_str = sentence_str.replace(
                    row[2], '[{}]({})'.format(row[3], row[2]))
        replaced_sentences.append(sentence_str)
    print('\n'.join(replaced_sentences))


if __name__ == '__main__':
    main()
