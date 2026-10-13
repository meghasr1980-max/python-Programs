def fibonacci_series(count):
    if count < 0:
        raise ValueError("Count cannot be negative")

    first, second = 0, 1
    result = []

    while len(result) < count:
        result.append(first)
        first, second = second, first + second

    return result


if __name__ == "__main__":
    count = int(input("Enter number of terms: "))
    print(fibonacci_series(count))