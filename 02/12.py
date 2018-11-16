def main():
    with open('hightemp.txt') as f, \
            open('col1.txt', 'w') as col1, \
            open('col2.txt', 'w') as col2:
        for l in f:
            col1.write(l.split("\t")[0]+"\n")
            col2.write(l.split("\t")[1]+"\n")


if __name__ == '__main__':
    main()
