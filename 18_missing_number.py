def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)


if __name__ == "__main__":
    values = list(map(int, input("Enter numbers separated by spaces: ").split()))
    n = int(input("Enter n: "))
    print("Missing number:", find_missing_number(values, n))