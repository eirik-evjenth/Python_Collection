import re

def first_word(text: str) -> str:

    # Find the first word
    match = re.search(r"\b\w+(?:'\w+)?\b", text)

    if match:
        return match.group()
    


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")