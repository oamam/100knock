def main():
    a = 'パトカー'
    b = 'タクシー'
    print(''.join([sa + sb for sa, sb in zip(a, b)]))

if __name__ == '__main__':
    main()
