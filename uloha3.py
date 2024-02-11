def is_palindrome(s):
    return s == s[::-1]


def nextPalindrome(from_num, radix, next_palindrome):
    if radix < 2 or radix > 36:
        return 0

    num = from_num + 1
    while True:
        num_str = format(num, '0' + str(radix))
        if is_palindrome(num_str):
            next_palindrome[0] = num
            return 1
        num += 1


# Příklad použití:
from_num = 17
radix = 10
next_palindrome = [0]  # Výstupní parametr, bude obsahovat nalezené číslo-palindrom
success = nextPalindrome(from_num, radix, next_palindrome)
if success:
    print("Nalezený palindrom:", next_palindrome[0])
else:
    print("Nepodařilo se najít palindrom.")
