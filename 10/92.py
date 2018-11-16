import numpy as np
import pickle
from scipy import io


def cos_sim(vec_a, vec_b):
    vec_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    if vec_ab != 0:
        return np.dot(vec_a, vec_b) / vec_ab
    else:
        return -1


def main():
    with open('dict_index_t', 'rb') as index_f:
        dict_index_t = pickle.load(index_f)
    matrix_x300 = io.loadmat('matrix_x300')['matrix_x300']

    with open('families.txt', 'rt') as input_f, \
            open('families_sim.txt', 'wt') as output_f:
        for line in input_f:
            max_sim = 0
            max_word = 0
            words = line.strip().split(' ')
            if words[0] not in dict_index_t or \
                    words[1] not in dict_index_t or \
                    words[2] not in dict_index_t:
                words.append('')
                words.append(-1)
                print(*words, sep=' ', end='\n', file=output_f)
                continue
            vec = matrix_x300[dict_index_t[words[1]]] - \
                matrix_x300[dict_index_t[words[0]]] + \
                matrix_x300[dict_index_t[words[2]]]
            for k, _ in dict_index_t.items():
                sim = cos_sim(vec, matrix_x300[dict_index_t[k]])
                if sim > max_sim:
                    max_sim = sim
                    max_word = k
            words.append(max_word)
            words.append(max_sim)
            print(*words, sep=' ', end='\n', file=output_f)


if __name__ == '__main__':
    main()
