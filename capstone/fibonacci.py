import sys
import getopt

def main(argv):
    nth_iteration = 0
    max_number = 0
    nth_chosen = False

    try:
        opts, args = getopt.getopt(argv, "hn:m:", ["nth-iteration=", "max-number="])
    except getopt.GetoptError:
        print("fibonacci.py -n <nth-iteration> | -m <max-number>")
        sys.exit(2)

    if args:
        print("fibonacci.py -n <nth-iteration> | -m <max-number>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in "-h":
            print("fibonacci.py -n <nth-iteration> | -m <max-number>")
            sys.exit(0)
        elif opt in ("-n", "--nth-iteration"):
            nth_iteration = int(arg)
            nth_chosen = True
        elif opt in ("-m", "--max-number") and nth_chosen:
            print("fibonacci.py -n <nth-iteration> | -m <max-number>")
            sys.exit(2)
        elif opt in ("-m", "--max-number"):
            max_number = int(arg)
        else:
            print("fibonacci.py -n <nth-iteration> | -m <max-number>")
            sys.exit(2)

    for fib in fibonacci(nth_iteration,max_number):
        print(fib)

    print("opts:", opts)
    print("args:", args)

def fibonacci(nth_iteration=0, max_number=0):
    """
    Caculate fibonacci sequence, return generator as a result
    :param nth_iteration:
    :param max_number:
    :return:
    """
    a = 0
    b = 1

    if nth_iteration:
        while nth_iteration > 0:
            nth_iteration -= 1
            a, b = b, a + b
            yield a
    elif max_number:
        while b < max_number:
            a, b = b, a + b
            yield a

if __name__=='__main__':
    main(sys.argv[1:])
    print("sys.argv[1:]:", sys.argv[1:])

#    for fib in fibonacci(10):
#        print(fib)
