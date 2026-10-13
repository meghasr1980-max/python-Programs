def sum_of_digits(number):
    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(number))