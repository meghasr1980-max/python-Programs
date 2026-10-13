def factorial(number):
    if number < 0:
        raise ValueError("Enter a non-negative integer")

    answer = 1
    for value in range(1, number + 1):
        answer *= value

    return answer


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Factorial:", factorial(number))