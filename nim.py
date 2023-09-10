size = 12
x_array = ['x'] * size
print(len(x_array))


def user():
    while True:
        try:
            user_input = input("Enter something less than 4: ")
            user_input_int = int(user_input)

            if user_input_int < 4:
                break
            else:
                print("less than 4  needed")
        except ValueError:
            print("input an int")   
    return user_input_int
    print("You entered:", user_input)

size = size - user()

print("There are",size,"balls left" )
print(x_array)


def dr_nim (inputsize):
    result = inputsize % 4
    return result

drnimtakes = dr_nim(size)
print("Dr nim takes", drnimtakes)

size = size - drnimtakes
print("size is now", size)

size = size - user()
print("size is now", size)

drnimtakes = dr_nim(size)
print("Dr nim takes", drnimtakes)

size = size - drnimtakes
print("size is now", size)

size = size - user()
print("size is now", size)

drnimtakes = dr_nim(size)
print("Dr nim takes", drnimtakes)

size = size - drnimtakes
print("size is now", size)

if size == 0:
    print("dr nim took the last ball")

