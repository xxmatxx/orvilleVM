def print_int(max_int):
    i = 0
    while (i < max_int):
        print(i)
        i = i + 1

print_int(3)

def power(x,p):
    i = 0
    temp = 1
    while(i < p):
        temp = temp * x
        i = i + 1
    return temp

print(power(3,4))

