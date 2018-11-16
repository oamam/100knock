import pickle
from scipy import io


def main():
    input_index_t = 'dict_index_t'
    input_matrix = 'matrix_x300'

    with open(input_index_t, 'rb') as data_file:
        dict_index_t = pickle.load(data_file)

    matrix_x300 = io.loadmat(input_matrix)['matrix_x300']
    print(matrix_x300[dict_index_t['United_States']])


if __name__ == '__main__':
    main()
