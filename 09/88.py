import pickle
from scipy import io
import numpy as np


def cos_sim(vec_a, vec_b):
    vec_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    if vec_ab != 0:
        return np.dot(vec_a, vec_b) / vec_ab
    else:
        return -1


def main():
    input_index_t = 'dict_index_t'
    input_matrix = 'matrix_x300'

    with open(input_index_t, 'rb') as data_file:
        dict_index_t = pickle.load(data_file)

    matrix_x300 = io.loadmat(input_matrix)['matrix_x300']

    england_sim = {}
    vec_a = matrix_x300[dict_index_t['England']]
    for k, _ in dict_index_t.items():
        vec_b = matrix_x300[dict_index_t[k]]
        england_sim[k] = cos_sim(vec_a, vec_b)
    print(sorted(england_sim.items(), key=lambda x: x[1], reverse=True)[1:11])


if __name__ == '__main__':
    main()
