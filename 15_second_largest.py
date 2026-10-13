def second_largest(numbers):
    unique = sorted(set(numbers))

    if len(unique) < 2:
        raise ValueError("Need at least two unique numbers")

    return unique[-2]


if __name__ == "__main__":
    values = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Second largest:", second_largest(values))