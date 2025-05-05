import random
import string

def generate_password():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 4:
            print("Password should be at least 4 characters long for better security.")
            return

        
        letters = string.ascii_letters  
        digits = string.digits          
        symbols = string.punctuation   

        
        all_chars = letters + digits + symbols

        
        password = ''.join(random.choice(all_chars) for _ in range(length))

      
        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid number.")

generate_password()
