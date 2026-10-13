def primes_in_range(start, end):
    primes = []

    for number in range(max(2, start), end + 1):
        prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                prime = False
                break

        if prime:
            primes.append(number)

    return primes


if __name__ == "__main__":
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    print(primes_in_range(start, end))