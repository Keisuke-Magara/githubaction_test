import os


def helloworld():
    files = os.listdir(path='../../.idea/')
    print(files)

if __name__ == '__main__':
    helloworld()