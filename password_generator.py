import string
import random

def generate_password(length = 12,use_uppercase = True, use_lowercase = True, use_digits = True, use_symbols = True):
    characters=""
    if use_uppercase:
        characters+=string.ascii_uppercase
    if use_lowercase:
        characters+=string.ascii_lowercase
    if use_digits:
        characters+=string.digits
    if use_symbols:
        characters+=string.punctuation
        
    if not characters:
        return "Error:No character types selected"
    password = "".join(random.choice(characters) for _ in range(length))
    return password
def main():    
    length=12
    use_uppercase=True
    use_lowercase=True
    use_digits=True
    use_symbols=True

    password = generate_password(12,use_uppercase,use_lowercase,use_digits,use_symbols)
    print("generate_password!")
    print("Your password is", password )
    
if __name__=="__main__":
    main()
