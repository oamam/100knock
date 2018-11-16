def main():
    with open('hightemp.txt') as f:
        for l in f:
            print(l.replace("\t", ' ').replace("\n", ''))


if __name__ == '__main__':
    main()
