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

    while True:
        
        print("Select the type of password you need: complex(Ab&7), alphabetical(Ab), numerical(123)")
        type_of = input()

        if type_of == "complex":
            break
        elif type_of == "alphabetical":
            break
        elif type_of == "numerical":
            break
            
        print("Please use one of the three options only")
        
    print(f"the arguments are: {read_word} and {read_num}. the password must be {type_of}")
    print("==============================================================================")

if __name__ == "__main__":
    main()