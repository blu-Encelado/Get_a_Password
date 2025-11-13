import sys


def main():
    print("#####----Get a Password----#####")
    comand = sys.argv

    word = comand[1]
    number = comand[2]
    print(number)

    for letter in word:
        if not letter.isalpha():
            raise ValueError("Please use a word with only letters as first argument")

    for digit in number:
        if not digit.isnumeric():
            raise ValueError("Please use a number as second argument")

    print(f"{word} // {number}")




if __name__ == "__main__":
    main()