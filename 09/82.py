import random
import os


def main():
    input_file = 'tokens81.txt'
    output_file = 'context.txt'
    if os.path.isfile(output_file):
        os.remove(output_file)
    with open(input_file, 'rt') as input_f, \
            open(output_file, mode='a') as output_f:
        for i, line in enumerate(input_f):
            tokens = line.strip().split(' ')
            for j, token in enumerate(tokens):
                d = random.randint(1, 5)
                for k in range(max(0, j - d), min(j + d + 1, len(tokens))):
                    if j != k:
                        print(
                            '{}\t{}'.format(token, tokens[k]),
                            end='\n',
                            file=output_f
                        )


if __name__ == '__main__':
    main()
