import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    artists = r.keys('*')
    c = 0
    for artist in artists:
        if r.get(artist).decode('utf-8') == 'Japan':
            c += 1
    print(c)


if __name__ == '__main__':
    main()
