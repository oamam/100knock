from scipy import io
import pickle
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def main():
    with open('dict_countries_t', 'rb') as f:
        dict_index_t = pickle.load(f)
    matrix_x300 = io.loadmat('matrix_countries_x300')['matrix_x300']

    t_sne = TSNE(perplexity=30, learning_rate=500).fit_transform(matrix_x300)
    print(t_sne)

    predicts = KMeans(n_clusters=5).fit_predict(matrix_x300)

    fig, ax = plt.subplots()
    cmap = plt.get_cmap('Set1')
    for index, label in enumerate(dict_index_t.keys()):
        if label == 'Namibia':
            continue
        cval = cmap(predicts[index] / 4)
        ax.scatter(t_sne[index, 0], t_sne[index, 1], marker='.', color=cval)
        ax.annotate(label, xy=(t_sne[index, 0], t_sne[index, 1]), color=cval)
    plt.show()


if __name__ == '__main__':
    main()
