from collections import Counter
import pickle


def main():
    input_file = 'context.txt'
    counter_tc = Counter()
    counter_t = Counter()
    counter_c = Counter()
    ftc = []
    ft = []
    fc = []
    with open(input_file, 'rt') as f:
        for i, line in enumerate(f, start=1):
            words = line.split('\t')
            ftc.append(line.strip())
            ft.append(words[0])
            fc.append(words[1])
            if i % 10000 == 0:
                counter_tc.update(ftc)
                counter_t.update(ft)
                counter_c.update(fc)
                ftc = []
                ft = []
                fc = []
    counter_tc.update(ftc)
    counter_t.update(ft)
    counter_c.update(fc)

    with open('tc_counter.dump', 'wb') as f:
        pickle.dump(counter_tc, f)
    with open('t_counter.dump', 'wb') as f:
        pickle.dump(counter_t, f)
    with open('c_counter.dump', 'wb') as f:
        pickle.dump(counter_c, f)

    print('N: {}'.format(i))


if __name__ == '__main__':
    main()
