from sklearn.cluster import KMeans
from scipy import io
import pickle


def main():
    with open('dict_countries_t', 'rb') as f:
        dict_index_t = pickle.load(f)
    matrix_x300 = io.loadmat('matrix_countries_x300')['matrix_x300']
    predict = KMeans(n_clusters=5).fit_predict(matrix_x300)
    print(sorted(zip(predict, dict_index_t.keys()),
                 key=lambda x: x[0], reverse=True))


if __name__ == '__main__':
    main()
