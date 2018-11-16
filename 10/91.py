def main():
    with open('analogy_evaluations.txt') as input_f, \
            open('families.txt', 'wt') as output_f:
        while True:
            line = input_f.readline()
            if ': family' not in line:
                continue
            while True:
                line = input_f.readline()
                if ': ' in line:
                    break
                print(line, end='', file=output_f)
            break


if __name__ == '__main__':
    main()
