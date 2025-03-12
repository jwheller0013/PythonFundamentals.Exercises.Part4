def number_input():
    number= input("Please enter a number between 0-30:\n")

    return number

def fibonnaci(a):
# recursive means calling the function in the function
# if int(a) < 0 or int(a) > 30:
#     print ("Try again following instructions")
    if a == 0:
        return 0
    if a == 1:
        return 1
    else:
        return fibonnaci(a-1) + fibonnaci(a -2)



number= int(number_input())
print(fibonnaci(number))
