def remove_duplicates(numbers):
    seen = set()
    result = []

    for number in numbers:
        if number not in seen:
            result.append(number)
            seen.add(number)

    return result


if __name__ == "__main__":
    values = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(remove_duplicates(values))