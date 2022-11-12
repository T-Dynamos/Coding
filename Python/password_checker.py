import string

def check_passsword(password : str,sp_chars = ["#","$","@"],max_lenght=16,mini_lenght=6) -> list:
    errors = []
    num = False
    sp_char = False
    lowercase = False
    upercase = False

    for letter in password:
        if letter in [str(number) for number in list(range(1,10))]:
            num = True
        if letter in string.ascii_lowercase:
            lowercase = True
        if letter in string.ascii_uppercase:
            upercase = True

    if lowercase == False:
        errors.append("Please include at least one lowercase letter")
    
    if upercase == False:
        errors.append("Please include at least one uppercase letter")
    
    if num == False:
        errors.append("Letter missing form 1-9")
    
    for char in sp_chars:
        if char in password:
            sp_char = True
            break
    
    if sp_char == False:
        errors.append("Special character missing")

    if len(password) < mini_lenght:
        errors.append("Minimum lenght 6 not provided")

    if len(password) >= max_lenght:
        errors.append("Maximum lenght is 16")

    return errors


password = "Rea#db3"
print(check_passsword(password))