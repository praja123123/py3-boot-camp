from random import randint

number_to_guess = randint(1,101)
#print('number to guess: ', number_to_guess)
previous_guess = None
guessed = False
number_of_tires = 0

while not guessed:
    number_gussed = int(input("Please, guess a number from 1 to 100:\n"))
    number_of_tires += 1
    if number_gussed == number_to_guess:
        guessed = True
        print(f'BINGO, you have guessed correctly with {number_of_tires} tire(s)!')
    elif number_gussed < 1 and number_gussed > 100:
        print('OUT OF BOUNDS')
    elif number_of_tires == 1:
        if abs(number_to_guess - number_gussed) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(previous_guess - number_to_guess) > abs(number_gussed - number_to_guess):
            print('WARMER!')
        else:
            print('COLDER!')
#    print('number to guess: ', number_to_guess)
#    print('previus guess: ', previous_guess)
#    print('number guessed: ', number_gussed)
    # last guess becomes the previoues guess
    previous_guess = number_gussed


