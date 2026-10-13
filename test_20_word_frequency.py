import sys
sys.path.insert(0, "Code")

import code_20_word_frequency as program

def test_word_frequency():
    assert program.word_frequency(
        "hello world hello"
    ) == {"hello": 2, "world": 1}

    assert program.word_frequency("python python") == {
        "python": 2
    }
    print("All test cases passed.")

if __name__ == "__main__":
    test_word_frequency()