from xml.etree import ElementTree
import pydot


def main():
    tree = ElementTree.parse('nlp.txt.xml')
    root = tree.getroot()
    document = root[0]
    sentences = document[1]

    for sentence in sentences:
        sentence_id = int(sentence.attrib['id'])
        dependencies = sentence[3]
        edges = []
        for dep in dependencies:
            if dep.get('type') == 'punct':
                continue
            edges.append((dep[0].text, dep[1].text))
        draw_tree(edges, sentence_id)


def draw_tree(edges, sentence_id):
    n = pydot.Node('node')
    n.fontname = "AppleGothic.ttf"
    n.fontsize = 9
    n.fontcolor = "blue"
    g = pydot.graph_from_edges(edges, directed=True)
    g.add_node(n)
    g.write_jpeg('57/{}.jpg'.format(sentence_id), prog='dot')


if __name__ == '__main__':
    main()
