def main():
    with open('families_sim.txt') as f:
        correct = 0
        for n, line in enumerate(f):
            cols = line.split(' ')
            if cols[3] == cols[4]:
                correct += 1
        print(correct / n)


if __name__ == '__main__':
    main()
