def largest_of_3(num1, num2, num3):
    one = num1 * (num1 >= num2 and num1 >= num3)
    two = num2 * (num2 >= num1 and num2 >= num3)
    three = num3 * (num3 >= num1 and num3 >= num2)
    #rint(one, two, three)
    return one + two + three


number1 = 10
number2 = 25
number3 = 15
result = largest_of_3(number1, number2, number3)
print(f"The largest number is: {result}")