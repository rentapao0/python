#
def find_largest():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    if a >= b and a >= c:
        then = ("A", a) 
    elif b >= a and b >= c:
        then = ("B", b)
    else:
        then = ("C", c)

    print(f"Letter {then[0]} is the largest with a value of {then[1]}.")

    find_largest()
