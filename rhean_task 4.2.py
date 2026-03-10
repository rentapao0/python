#
x = 300

print("Find the closest number to", x, "in the list:")

    def my_function():
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = int(input("Enter the third number: "))

        if a == b == c:
            print(f"A is {a}, B is {b}, and C is {c}. All numbers are all equal.")
            return

        nums = {'A': a, 'B': b, 'C': c}
        closest = min(nums, key=lambda k: abs(x - nums[k]))

       print(f"Letter {closest} or {nums[closest]} is the closest to {x}.")

if __name__ == "__main__":
    my_function()
