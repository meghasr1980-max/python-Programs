def is_palindrome_number(number):
    if number < 0:
        return False

    original = number
    reversed_num = 0

    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10

    return original == reversed_num


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(is_palindrome_number(number))