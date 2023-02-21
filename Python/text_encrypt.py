import string


def encrypt_text(string_value: str, sn=4) -> str:
    string_list = {}
    for letter, number in zip(string.ascii_lowercase, range(1, 27)):
        string_list[letter] = (string.ascii_lowercase + string.ascii_lowercase[:sn])[
            number + sn - 1
        ]
    text = []
    for i in string_value:
        text.append(string_list[i]) if i != " " else text.append(" ")

    return "".join(text)


print(encrypt_text("aradhya"))
