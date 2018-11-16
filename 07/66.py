from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client.knock
    artists = db.artists
    result = artists.find({'area': 'Japan'}).count()
    print(result)


if __name__ == '__main__':
    main()
