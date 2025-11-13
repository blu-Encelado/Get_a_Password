import sys
from config import *

def main():
    print("#####----Get a Password----#####")
    
    word_is_valid = False
    num_is_valid = False
    
    while not word_is_valid:
        
        print("write a word (letters only)")
        read_word = input()

        if read_word != "":
            i = 0
            for letter in read_word:
                if not letter.isalpha():
                    i += 1
            
            if i != 0:
                print("Please use a word with only letters as first argument, try again")
                    
            word_is_valid = (i == 0)
        print("word needed")
                
    print(f"the word is: {read_word}")

    while not num_is_valid:
        
        print("write a number (digits only)")
        read_num = input()

        if read_num != "":
            j = 0
            for digit in read_num:
                if not digit.isnumeric():
                    j += 1
            
            if j != 0:
                print("Please use a number as second argument, try again")
                
            num_is_valid = (j == 0)
        print("number needed")
        
        
    print(f"the arguments are: {read_word} and {read_num}")



if __name__ == "__main__":
    main()