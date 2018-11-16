import word2vec
from collections import OrderedDict
import numpy as np
import pickle
from scipy import io


def main():
    train_file = 'tokens81.txt'
    output_file = 'vectors.txt'
    maxtrix_file = 'matrix_x300'
    dict_index_file = 'dict_index_t'
    word2vec.word2vec(train=train_file, output=output_file,
                      size=300, threads=3, binary=0)

    with open(output_file, 'rt') as f:
        status = f.readline().split(' ')
        size_dict = int(status[0])
        size_x = int(status[1])

        dict_index_t = OrderedDict()
        matrix_x = np.zeros([size_dict, size_x], dtype=np.float64)

        for i, line in enumerate(f):
            vecs = line.strip().split(' ')
            dict_index_t[vecs[0]] = i
            matrix_x[i] = vecs[1:]

    io.savemat(maxtrix_file, {'matrix_x300': matrix_x})
    with open(dict_index_file, 'wb') as f:
        pickle.dump(dict_index_t, f)


if __name__ == '__main__':
    main()
