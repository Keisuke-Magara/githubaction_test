import os


def helloworld():
    files = os.listdir(path='../../')
    print(files)

if __name__ == '__main__':
    helloworld()