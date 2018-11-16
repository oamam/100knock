def main():
    c = 0
    with open('hightemp.txt') as f:
        for l in f:
            c += 1
    print(c)


if __name__ == '__main__':
    main()
