import pymongo
from pymongo import MongoClient
import gzip
import json


def main():
    client = MongoClient('localhost', 27017)
    db = client.knock
    artists = db.artists
    with gzip.open('artist.json.gz', 'rt') as f:
        temp = []
        c = 0
        for l in f:
            temp.append(json.loads(l))
            if len(temp) >= 10000:
                artists.insert_many(temp)
                temp = []
                c += 10000
                print(c)
    artists.create_index([('name', pymongo.ASCENDING)])
    artists.create_index([('aliases.name', pymongo.ASCENDING)])
    artists.create_index([('tags.value', pymongo.ASCENDING)])
    artists.create_index([('rating.value', pymongo.ASCENDING)])


if __name__ == '__main__':
    main()
