from collections import Counter
from collections import OrderedDict
from scipy import sparse, io
import math
import pickle


def main():
    input_file = 'context.txt'
    counter_tc = Counter()
    counter_t = Counter()
    counter_c = Counter()
    tc_arr = []
    t_arr = []
    c_arr = []
    N = 68083972
    with open(input_file, 'rt') as f:
        for i, line in enumerate(f, start=1):
            words = line.strip().split('\t')
            tc_arr.append(line.strip())
            t_arr.append(words[0])
            c_arr.append(words[1])
            if i % 10000 == 0:
                counter_tc.update(tc_arr)
                counter_t.update(t_arr)
                counter_c.update(c_arr)
                tc_arr = []
                t_arr = []
                c_arr = []
    counter_tc.update(tc_arr)
    counter_t.update(t_arr)
    counter_c.update(c_arr)

    dict_index_t = OrderedDict((key, i)
                               for i, key in enumerate(counter_t.keys()))
    dict_index_c = OrderedDict((key, i)
                               for i, key in enumerate(counter_c.keys()))

    size_t = len(dict_index_t)
    size_c = len(dict_index_c)
    matrix_x = sparse.lil_matrix((size_t, size_c))

    for k, f_tc in counter_tc.items():
        if f_tc >= 10:
            tokens = k.split('\t')
            t = tokens[0]
            c = tokens[1]
            ppmi = max(math.log((N * f_tc) / (counter_t[t] * counter_c[c])), 0)
            matrix_x[dict_index_t[t], dict_index_c[c]] = ppmi

    io.savemat('matrix_x', {'matrix_x': matrix_x})
    with open('dict_index_t', 'wb') as f:
        pickle.dump(dict_index_t, f)


if __name__ == '__main__':
    main()
