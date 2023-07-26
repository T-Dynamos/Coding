def validate_password(password):
    errors = []
    ___ = lambda _ : not any([__ in password for __ in _])
    checkers = [
        lambda : "lenght must be greator then or equal to 8" if len(password) <= 8 else None,
        lambda : "lenght must be shorter then or equal to 16" if len(password) >= 16 else None,
        lambda : "must cointain a special character in one of '$@#*%'" if ___("$@#*%") else None,
        lambda : "must cointain a capital letter" if ___("ABCDEFGHIJKLMNOPQRSTUVWXYZ") else None,
        lambda : "must cointain a lowercase letter" if ___("abcdefghijklmnopqrstuvwxyz") else None,
        lambda : "must cointain a numeric character" if ___("123456789") else None,
    ]
    for _ in checkers:
        __ = _()
        if __ is not None:
            errors.append(__)
    return errors

errors = validate_password(password = "$AnshDadwal69")

if len(errors) != 0:
    print("Your code has following errors: ")
    for count, error in enumerate(errors):
        print("{}. Password {}".format(count + 1 , error))
else:
    print("Password looks good!")
