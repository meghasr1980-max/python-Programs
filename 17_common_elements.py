def common_elements(first, second):
    second_values = set(second)
    result = []

    for value in first:
        if value in second_values and value not in result:
            result.append(value)

    return result


if __name__ == "__main__":
    first = list(map(int, input("First list: ").split()))
    second = list(map(int, input("Second list: ").split()))
    print(common_elements(first, second))