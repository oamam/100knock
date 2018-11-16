def main():
    print(xyz(12, '気温', 22.4))


def xyz(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)


if __name__ == '__main__':
    main()
