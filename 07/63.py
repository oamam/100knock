import json
import redis
import gzip


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    r.flushall()
    with gzip.open('artist.json.gz', 'rt') as f:
        for l in f:
            d = json.loads(l)
            if 'name' in d and 'tags' in d:
                for tag in d['tags']:
                    r.rpush(
                        d['name'],
                        d['id'],
                        tag['count'],
                        tag['value']
                    )
    keyword = input('アーティスト名 > ')
    tags = r.lrange(keyword, 0, -1)
    aid = 0
    for i in range(0, len(tags), 3):
        if aid != tags[i]:
            print('{}:{}'.format(keyword, tags[i].decode('utf-8')))
            aid = tags[i]
        print('\t{}({})'.format(
            tags[i+2].decode('utf-8'),
            tags[i+1].decode('utf-8')
        ))


if __name__ == '__main__':
    main()
