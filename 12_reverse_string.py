def reverse_string(text):
    characters = list(text)
    characters.reverse()
    return "".join(characters)


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed:", reverse_string(text))