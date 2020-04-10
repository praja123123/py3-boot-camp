#print('__name__:',__name__)

def add(x, y=3):
    return x + y

def multiply(x, y=3):
    return x * y

if __name__ == '__main__':
    print("2 + 3 =", add(2,3))