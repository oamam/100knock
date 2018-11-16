from xml.etree import ElementTree


def main():
    tree = ElementTree.parse('nlp.txt.xml')
    root = tree.getroot()
    document = root[0]
    sentences = document[1]
    for sentence in sentences:
        tokens = sentence[0]
        for token in tokens:
            print('{}\t{}\t{}'.format(
                token[0].text, token[1].text, token[4].text))


if __name__ == '__main__':
    main()
