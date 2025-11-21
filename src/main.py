from config import *
from magic import evaluate_pass

def main():
    print("#####----Get a Password----#####")
    
    while True:
        
        print("write a number (digits only)")
        read_num = input().strip()

        if read_num.isnumeric():
            break
            
        print("Please use one number as second argument, try again")

    while True:
        
        print("Select the type of password you need: complex(Ab&7), alphabetical(Ab), numerical(123), or alphanumerical(Ab12)")
        type_of = input().strip()

        if type_of == "complex":
            break
        elif type_of == "alphabetical":
            break
        elif type_of == "numerical":
            break
        elif type_of == "alphanumerical":
            break
            
        print("Please use one of the three options only")
        
    print(f"the arguments are: of length {read_num}. the password must be {type_of}")
    print(f"pass: {evaluate_pass(read_num, type_of)}")
    print("==============================================================================")


if __name__ == "__main__":
    main()