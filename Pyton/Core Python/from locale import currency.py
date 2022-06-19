
def fibonachi(number):
    if number == 0 or number==-1:
        return 0
    elif number == 1:
        return 1
    return fibonachi(number-1)+fibonachi(number-2)

print(fibonachi(32))