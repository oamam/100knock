import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    keyword = input('アーティスト名 > ')
    artists = r.keys(keyword + '*')
    for artist in artists:
        print('{} > {}'.format(artist.decode(
            'utf-8'), r.get(artist).decode('utf-8')))


if __name__ == '__main__':
    main()
