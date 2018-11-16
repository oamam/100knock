import os


def main():
    input_file = 'tokens80.txt'
    output_file = 'tokens81.txt'
    countries_file = 'countries.txt'
    if os.path.isfile(output_file):
        os.remove(output_file)
    with open(input_file, 'rt') as input_f, \
            open(countries_file, mode='rt') as countries_f, \
            open(output_file, mode='wt') as output_f:
        countries = countries_f.readlines()
        countries = [country.strip() for country in countries]
        for line in input_f:
            result = []
            tokens = line.split(' ')
            i = 0
            found = False
            while len(tokens) > i:
                for country in countries:
                    country_words = country.split(' ')
                    if tokens[i] != country_words[0]:
                        continue
                    ii = len(country_words)
                    if ' '.join(tokens[i: i+ii]) == country:
                        result.append('_'.join(tokens[i: i+ii]))
                        found = True
                        break
                if found is False:
                    w = tokens[i]
                    if len(w) > 0:
                        result.append(w)
                    i += 1
                else:
                    i += ii
                    found = False

            print(*result, sep=' ', end='', file=output_f)


if __name__ == '__main__':
    main()
