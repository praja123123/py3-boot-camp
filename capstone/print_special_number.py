import math

def get_n_digits(special_number):
    """
    Function gets the input digit number from the user,
    which tells how many numbers of pi/e needs to be displayed
    :param special_number:
    :return n_digits:
    """
    n_digits = -1

    while n_digits < 0 or n_digits > 15:
        try:
            n_digits = int(input("Please, specify how many decimal numbers (range is: 0..15) need to be displayed of " +
                                 "the special number {}: ".format(special_number.upper())))
        except ValueError:
            print("Wrong characters' input, should be integer number.")
        except:
            print("Something went wrong...")
            break

    return n_digits

def n_decimals(n_digits, special_number='PI'):
    """
    Function calculates only n digits form a special number (pi, e)
    :param n_digits:
    :param special_number:
    :return result:
    """
    if special_number.upper()=='PI':
        number = math.pi
    elif special_number.upper()=='E':
        number = math.e
    else:
        print("Special number not supported")
        return None

    if n_digits == 0:
        result = int(math.modf(number)[1])
    else:
        result = float("{:.{prec}f}".format(number, prec=n_digits))

    return result

if __name__ == '__main__':

    n_digits = get_n_digits('pi')
    print(n_decimals(n_digits, 'pi'))

    n_digits = get_n_digits('e')
    print(n_decimals(n_digits,'e'))
