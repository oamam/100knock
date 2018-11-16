def main():
    ll = ''
    with open('col1.txt', 'r') as col1, \
            open('col2.txt', 'r') as col2:
        for l, ll in zip(col1, col2):
            print("{}\t{}".format(l.replace("\n", ''), ll.replace("\n", '')))


if __name__ == '__main__':
    main()
