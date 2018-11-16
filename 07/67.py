from pymongo import MongoClient


def main():
    aliase = input('アーティス別名 > ')
    client = MongoClient('localhost', 27017)
    db = client.knock
    artists = db.artists
    result = artists.find({'aliases.name': aliase})
    for r in result:
        print('{}'.format(r['name']))


if __name__ == '__main__':
    main()
