def main():
    sentence = 'Now I need a drink, alcoholic of course ' \
            'after the heavy lectures involving quantum mechanics.'
    print([
        len(word) - word.count(',') - word.count('.')
        for word in sentence.split(' ')
    ])

if __name__ == '__main__':
    main()
