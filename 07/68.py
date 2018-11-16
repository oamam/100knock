import pymongo
from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client.knock
    artists = db.artists
    result = artists.find({'tags.value': 'dance'}).sort(
        'rating.count', pymongo.DESCENDING)
    for r in result[:10]:
        print('{}({})'.format(r['name'], r['rating']['count']))


if __name__ == '__main__':
    main()
