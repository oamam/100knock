from xml.etree import ElementTree


def main():
    tree = ElementTree.parse('nlp.txt.xml')
    root = tree.getroot()
    document = root[0]
    sentences = document[1]
    for sentence in sentences:
        tokens = sentence[0]
        for token in tokens:
            if token[5].text == 'PERSON':
                print(token[0].text)


if __name__ == '__main__':
    main()
