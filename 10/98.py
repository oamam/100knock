from scipy import io
import pickle
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt


def main():
    with open('dict_countries_t', 'rb') as f:
        dict_index_t = pickle.load(f)
    matrix_x300 = io.loadmat('matrix_countries_x300')['matrix_x300']

    w = ward(matrix_x300)
    print(w)

    dendrogram(w, labels=list(dict_index_t.keys()), leaf_font_size=8)
    plt.show()


if __name__ == '__main__':
    main()
