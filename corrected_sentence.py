# The function correct_sentence receives one sentence as input.
# It should return a corrected copy of it so that it always starts with a capital letter
# and ends with a period.

# Note that not all corrections are necessary. If the sentence already ends with a period,
# adding another one is not needed; it will be considered an error.

# Input arguments: string.
# Output arguments: string.

# Replace pass with your solution.

def correct_sentence(text):
    if text[0].islower():
        corrected_copy = text[0].upper() + text[1:]
    else:
        corrected_copy = text

    if text[-1] != ".":
        corrected_copy += "."
    return corrected_copy


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
