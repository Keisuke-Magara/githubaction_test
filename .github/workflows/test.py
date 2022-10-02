def helloworld():
    with open(file='../../pubspec.yaml') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    helloworld()