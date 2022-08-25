# Proving the F***ing theorm 
# Made by Ansh Dadwal and Krrish Kashap
# Do you get it?

no = input("Enter the number: ")

if len(no) > 2 or len(no) == 1 :
    print("Please provide with a 2 digit no.")
    exit()

def add_lower(no) -> str:
    if len(no) == 3:
        return no+" "
    elif len(no) == 2:
        return " "+no+" "
    elif len(no) == 4:
        return no
    else:
        return "  "+no
        

def calc_square(no) -> int:
    print("\n")
    last_digit = int(str(no)[1:])
    first_digit = int(str(no)[:1])
    print("[STEP 1]: Split Terms ",end="\n\n")
    setup = (str(first_digit**2) if first_digit**2 > 9 else "0"+str(first_digit**2)) + " | " + (str(last_digit**2) if last_digit**2 > 9 else "0"+str(last_digit**2))
    print(f"{first_digit} | {last_digit}",end="\n\n\n")
    print(f"[STEP 2]: Multiply 2 by {last_digit}(Last Digit) and then multiply answer by {first_digit}(First Digit)\n")
    print(f"{first_digit} | {last_digit}  <-- {last_digit} x {first_digit} x 2 = {last_digit*first_digit*2}"+"\n^              ^\n|______________|\n\n")
    print("[STEP 3]: Square both digits")
    print("\nNote : If the square of last number is in one digit, then use 0 at tens place ")
    print(f"\n{first_digit} | {last_digit}\n\n|   |\nv   v\n\n"+setup,end="\n")
    print("\n\n[STEP 4]: Add numbers, living a number at last")
    setup2 = str(setup.replace(" | ","")) if len(str(setup.replace(" | ",""))) == 4 else "0"+str(setup.replace(" | ","")) 
    print(f"\n {str(setup2)} \n+{add_lower(str(last_digit*first_digit*2))} \n ---- \n {add_lower(str(int(last_digit*first_digit*2)+int(str(setup2)[:-1])))[:-1]}{str(setup2)[len(str(setup2))-1]} <-- Answer!")
print("The F***ing Theorm | Ansh Dadwal and Krish Kashap")
calc_square(no)
