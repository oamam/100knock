from collections import OrderedDict
import pickle
from scipy import io


def main():
    with open('dict_index_t', 'rb') as index_f:
        dict_index_t = pickle.load(index_f)
    matrix_x300 = io.loadmat('matrix_x300')['matrix_x300']

    with open('countries.txt', 'rt') as countries_f:
        dict_countries_index_t = OrderedDict()
        matrix = []
        ii = 0
        for country in countries_f:
            country = country.replace(' ', '_').strip()
            for k, i in dict_index_t.items():
                if k == country:
                    matrix.append(matrix_x300[i])
                    dict_countries_index_t[k] = ii
                    ii += 1

        io.savemat('matrix_countries_x300', {'matrix_x300': matrix})
        with open('dict_countries_t', 'wb') as f:
            pickle.dump(dict_countries_index_t, f)


if __name__ == '__main__':
    main()
