from xml.etree import ElementTree


def main():
    tree = ElementTree.parse('nlp.txt.xml')
    root = tree.getroot()
    document = root[0]
    sentences = document[1]

    for sentence in sentences:
        dependencies = sentence[3]
        preds = {}
        subjs = {}
        objs = {}
        for dep in dependencies:
            idx = dep[0].get('idx')
            if dep.get('type') == 'nsubj':
                preds[idx] = dep[0].text
                subjs[idx] = dep[1].text
            elif dep.get('type') == 'dobj':
                preds[idx] = dep[0].text
                objs[idx] = dep[1].text
        for idx, pred in preds.items():
            if idx in subjs and idx in objs:
                print('{}\t{}\t{}'.format(subjs[idx], pred, objs[idx]))


if __name__ == '__main__':
    main()
