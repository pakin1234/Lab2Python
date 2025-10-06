'''1. Написать функцию, которая проверяет является ли строка палиндромом.'''

def is_palindrome(text: str) -> bool:
    text = ''.join(filter(str.isalnum, text.casefold()))
    return (text == text[::-1] and len(text) != 0)
    
def main():
    input_string = input()
    if is_palindrome(input_string):
        print(f"{input_string} палиндром")
    else:
        print(f"{input_string} не палиндром")

if __name__ == "__main__":
    main()
