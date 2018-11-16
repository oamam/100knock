def main():
    n = int(input('N: '))
    with open('hightemp.txt', 'r') as f:
        lines = f.readlines()
        for l in lines[-n:]:
            print(l.rstrip())


if __name__ == '__main__':
    main()
