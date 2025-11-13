from config import *

def main():
    print("#####----Get a Password----#####")
    
    while True:
        
        print("write a word (letters only)")
        read_word = input()

        if read_word.isalpha():
            break
            
        print("Please use one word with only letters as first argument, try again")
    
    print(f"the word is: {read_word}")

    while True:
        
        print("write a number (digits only)")
        read_num = input()

        if read_num.isnumeric():
            break
            
        print("Please use one number as second argument, try again")
        
    print(f"the arguments are: {read_word} and {read_num}")
    print("==============================================")

if __name__ == "__main__":
    main()