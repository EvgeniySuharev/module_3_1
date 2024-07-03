def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    res = len(string), string.upper(), string.lower()
    return res


def is_contains(string, list_of_strings):
    count_calls()
    string = string.lower()
    for i in list_of_strings:
        obj = i.lower()
        if string == obj:
            return True


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)