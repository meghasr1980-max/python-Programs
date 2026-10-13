def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Prime" if is_prime(number) else "Not prime")