from nltk import stem
import numpy as np
from sklearn.linear_model import LogisticRegression


def main():
    lr = learn()
    features_ranking(lr)


def learn():
    sentiments = read_file('sentiments.txt')
    features = read_file('features.txt')

    X = explanatory_variables(sentiments, features)
    y = purpose_variables(sentiments)

    lr = LogisticRegression()
    lr.fit(X, y)

    return lr


def features_ranking(lr):
    features = read_file('features.txt')
    idxs = np.argsort(lr.coef_[0])
    print('=== best 10 ===')
    for i in reversed(idxs[-10:]):
        print('{} {}'.format(lr.coef_[0][i], features[i]))
    print('\n=== worst 10 ===')
    for i in idxs[:10]:
        print('{} {}'.format(lr.coef_[0][i], features[i]))


def read_file(path):
    with open(path, encoding='cp1252') as f:
        return [w.strip() for w in f.readlines()]


def explanatory_variables(sentiments, features, debug=False):
    stemmer = stem.PorterStemmer()
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
    X = np.zeros([len(sentiments), len(features) + 1], dtype=np.float64)
    X[:, 0] = 1
    for i, sentiment in enumerate(sentiments):
        for word in sentiment.split(' '):
            w = word.lower()
            if w in stop_words:
                continue
            if len(w) == 1 and w not in ['!', '?']:
                continue
            w = stemmer.stem(w)
            if w not in features:
                continue
            ii = features.index(w)
            X[i][ii] = 1
    return X


def purpose_variables(sentiments):
    y = np.zeros(len(sentiments), dtype=np.float64)
    for i, sentiment in enumerate(sentiments):
        if sentiment[:2] == '+1':
            y[i] = 1
    return y


if __name__ == '__main__':
    main()
