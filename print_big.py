def print_big(letter):
    patterns = {1: "*    ", 2: " *   ", 3: "  *  ", 4: "   * ", 5: "    *", 6: "*   *", 7: " * * ", 8: "*****",
                9: " ****", 10: "**** "}
    letters_mapping = {"a": (3, 7, 8, 6, 6), "b": (10, 6, 10, 6, 10), "c": (9, 1, 1, 1, 9)}

    #letter = input("Plesas give the letter: 'a' or 'b' or 'c'\n")
    mapping = letters_mapping[letter]

    for asterisk_map in mapping:
        print(patterns[asterisk_map])

print_big('a')
print('\n')
print_big('b')
print('\n')
print_big('c')

'l'.isalpha()
