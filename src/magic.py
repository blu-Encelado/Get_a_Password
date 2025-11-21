from config import*
import random

def evaluate_pass(num, type_of):
    match type_of:
        case "complex":
            return get_complex(num)
        case "alphabetical":
            return get_alphabetical( num)
        case "numerical":
            return get_numerical(num)
        case "alphanumerical":
            return get_alphanumerical(num)
        case _:
            raise ValueError("Wrong type_of passed")
        

def get_complex(num):
    password = ""
    index = 0
    while index <= int(num):
        r_list = random.randrange(0, 3)
        match r_list:
            case 0:
                list = ALPH
            case 1:
                list = NUM
            case 2:
                list = SYM
            case _:
                raise ValueError("bad roll")
        password += random_element(r_list, list)
        index += 1
    return password

def get_alphabetical(num):
    password = ""
    index = 0
    while index <= int(num):

        password += random_element(0, ALPH)

        index += 1
    return password

def get_numerical(num):
    password = ""
    index = 0
    while index <= int(num):
        
        password += random_element(1, NUM)

        index += 1
    return password

def get_alphanumerical(num):
    password = ""
    index = 0
    while index <= int(num):
        r_list = random.randrange(0, 2)
        match r_list:
            case 0:
                list = ALPH
            case 1:
                list = NUM
            case _:
                raise ValueError("bad roll")
        password += random_element(r_list, list)
        index += 1
    return password

def random_element(type = 0, array = None):
    is_cap = False
    if type == 0:
        is_cap = int(random.randint(0, 10)) % 2 == 0
            
    first = 0
    last = len(array)

    r_ind = random.randrange(first, last)

    if is_cap:
        return str(array[r_ind]).capitalize()
    else:
        return str(array[r_ind])
    