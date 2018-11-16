def main():
    print(cipher('fsadf9e8kdhsadie'))


def cipher(str):
    r = ''
    for s in str:
        if s.islower:
            r += chr(219 - ord(s))
        else:
            r += s
    return r


if __name__ == '__main__':
    main()
