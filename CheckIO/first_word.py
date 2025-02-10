def first_word(text: str) -> str:
    
    # return text.split()[0]

    index = text.find(" ")
    if index == -1:
        return text
    return text[:index]



print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")