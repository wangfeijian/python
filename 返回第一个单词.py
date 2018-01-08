def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    num = 0
    for i in text:
        if i.isalpha():
            break
        num += 1
    str_test = ''
    for j in range(num, len(text)):
        if text[j].isalpha() or text[j] == "'":
            str_test = str_test + text[j]
        else:
            break
    print(str_test)
    return str_test


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
