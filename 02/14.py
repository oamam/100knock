def main():
    n = int(input('N: '))
    with open('hightemp.txt', 'r') as f:
        for l in f:
            if n == 0:
                break
            print(l.rstrip())
            n = n - 1


if __name__ == '__main__':
    main()
