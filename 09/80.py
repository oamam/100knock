import bz2


def main():
    input_file = 'enwiki-20150112-400-r100-10576.txt.bz2'
    output_file = 'tokens80.txt'
    with bz2.open(input_file, 'rt') as input_f, \
            open(output_file, mode='a') as output_f:
        for line in input_f:
            tokens = []
            for token in line.split(' '):
                token = token.strip().strip('.,!?;:()[]\'"')
                if len(token) == 0:
                    continue
                tokens.append(token)
            print(*tokens, sep=' ', end='\n', file=output_f)


if __name__ == '__main__':
    main()
