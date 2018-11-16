from sklearn.decomposition import TruncatedSVD
from scipy import io


def main():
    matrix_x = io.loadmat('matrix_x')['matrix_x']
    clf = TruncatedSVD(300)
    matrix_x300 = clf.fit_transform(matrix_x)
    io.savemat('matrix_x300', {'matrix_x300': matrix_x300})


if __name__ == '__main__':
    main()
