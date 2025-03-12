def number_input():
    number= input("Please enter a number between 0-30:\n")

    return number

def fibonnaci(a):
    if a < 0 or a > 30:
        print ("Try again following instructions")

    else:
        nums = [0, 1]
        for i in range(2,a+1,1):
            nums2 = [nums[i-1] + nums[i-2]]
            nums = nums + nums2
        print ("Fibonacci of " + str(a) + " is " + str(nums[a]))

number= number_input()
fibonnaci(int(number))