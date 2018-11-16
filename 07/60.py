import json
import redis
import gzip


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.flushall()
    with gzip.open('artist.json.gz', 'rt') as f:
        for l in f:
            d = json.loads(l)
            if 'name' in d and 'area' in d:
                r.set('{}:{}'.format(d['name'], str(d['id'])), d['area'])


if __name__ == '__main__':
    main()
