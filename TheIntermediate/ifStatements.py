
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male, but are tall")
else:
    print("You are either not a male and not tall")
    print("Womp Womp")


print("--------------------------------------------------------")

def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(max_num(4, 5, 8))