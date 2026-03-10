#
while True:
    input_password = input("password: ")
    has_letter = False
    has_number = False

    for char in input_password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True

    if has_letter and has_number:
        print("Password is valid.")
        break
    else:
        print("Access denied.")
