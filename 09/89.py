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

    mix_sim = {}
    vec_spain = matrix_x300[dict_index_t['Spain']]
    vec_madrid = matrix_x300[dict_index_t['Madrid']]
    vec_athens = matrix_x300[dict_index_t['Athens']]
    vec_mix = vec_spain - vec_madrid + vec_athens
    for k, _ in dict_index_t.items():
        vec_x = matrix_x300[dict_index_t[k]]
        mix_sim[k] = cos_sim(vec_mix, vec_x)
    print(sorted(mix_sim.items(), key=lambda x: x[1], reverse=True)[:10])


if __name__ == '__main__':
    main()
