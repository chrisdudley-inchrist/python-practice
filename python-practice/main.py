


def count_vowels(text: str) -> int:
    text = text.lower()
    count = 0

    for letter in text:
        if letter in 'aeiou':
            count += 1
    return count

if __name__ == '__main__':
    user_input = input('Enter text to count vowels: ')
    total = count_vowels(user_input)
    print(f'{user_input} has {total} vowels')