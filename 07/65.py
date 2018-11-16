from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client.knock
    artists = db.artists
    results = artists.find({'name': 'Queen'})
    for r in results:
        print(r)


if __name__ == '__main__':
    main()
