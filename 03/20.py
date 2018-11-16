import gzip
import json


def main():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for l in f:
            j = json.loads(l)
            if j['title'] == 'イギリス':
                print(j['text'])
                break


if __name__ == '__main__':
    main()
