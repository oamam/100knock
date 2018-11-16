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

    with open('wordsim353/combined.tab', 'rt') as input_f, \
            open('combined_sim.txt', 'wt') as output_f:
        input_f.readline()
        for line in input_f:
            cols = line.strip().split('\t')
            if cols[0] not in dict_index_t or \
                    cols[1] not in dict_index_t:
                cols.append('')
                cols.append(-1)
                print(*cols, sep=' ', end='\n', file=output_f)
                continue
            sim = cos_sim(
                matrix_x300[dict_index_t[cols[0]]],
                matrix_x300[dict_index_t[cols[1]]]
            )
            cols.append(sim)
            print(*cols, sep=' ', end='\n', file=output_f)


if __name__ == '__main__':
    main()
