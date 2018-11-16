from nltk import stem
from collections import Counter


def main():
    negs = read_file('rt-polaritydata/rt-polarity.neg')
    poss = read_file('rt-polaritydata/rt-polarity.pos')
    sentiments = negs + poss
    words_counter = extract_features(sentiments)
    features = [word for word, count in words_counter.items() if count > 6]
    write_file(features)


def read_file(path):
    with open(path, encoding='cp1252') as f:
        return f.readlines()


def write_file(features):
    with open('features.txt', mode='w') as f:
        for w in features:
            f.write(w + '\n')


def extract_features(sentiments):
    stemmer = stem.PorterStemmer()
    words_counter = Counter()
    stop_words = (
        'a,able,about,across,after,all,almost,also,am,among,an,and,any,'
        'are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,'
        'does,either,else,ever,every,for,from,get,got,had,has,have,he,'
        'her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,'
        'let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,'
        'off,often,on,only,or,other,our,own,rather,said,say,says,she,'
        'should,since,so,some,than,that,the,their,them,then,there,these,'
        'they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,'
        'which,while,who,whom,why,will,with,would,yet,you,your'
    ).split(',')

    for sentiment in sentiments:
        for word in sentiment.split(' '):
            w = word.lower()
            if w in stop_words:
                continue
            if len(w) == 1 and w not in ['!', '?']:
                continue
            w = stemmer.stem(w)
            words_counter.update([w])

    return words_counter


if __name__ == '__main__':
    main()
