def main():
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.' \
                'New Nations Might Also Sign Peace Security Clause.' \
                'Arthur King Can.'
    words = sentence.split(' ')
    d = {}
    for i, w in enumerate(words, 1):
        if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            d[w[0]] = i
        else:
            d[w[0:2]] = i
    print(d)

if __name__ == '__main__':
    main()
