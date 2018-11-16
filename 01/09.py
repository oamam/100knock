import random


def main():
    a = "I couldn't believe that I could actually understand " \
        "what I was reading : the phenomenal power of the human mind ."
    b = []
    for s in a.split(' '):
        if 4 >= len(s):
            b.append(s)
        else:
            b.append(
                s[0] + ''.join(random.sample(s[1:-1], len(s[1:-1]))) + s[-1]
            )
    print(' '.join(b))

if __name__ == '__main__':
    main()
