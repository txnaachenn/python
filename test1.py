#input two numbers and save the two numbers into 2 number, then compare a and b then print the biggest one

# a = int(input('enter number a: '))
# b = int(input('enter number b: '))

# if a>b:
#     print(a, 'is the biggest number')
# else:
#     print(b, 'is the biggest number')

# if b>a:
#     print(b, 'is the biggest number')


# def square(x):
#     return x*x

# print('the square value of %d is %d.' % (3, square(3)))
# print('the square value of %d is %d.' % (6, square(6)))
# print('the square value of %d is %d.' % (9, square(9)))


# def sumofsquare(a, b):
#     return a*a+b*b
# print('the sum of the square value is %d.' % (sumofsquare(3, 5)))
# print('the sum of the square value is %d.' % (sumofsquare(2, 9)))

# sumOfSquare(2,3) # 2*2+3*3 = 13
# sumOfSquare(4,7) # 4*4+7*7 = 65


#homework 1
#make a function which name is sum, it will calculate the total of three values.
#for example:
#print(sum(3, 6, 8)) #17
#print(sum(1 , 9, 8)) #18


# def sum(num1, num2, num3):
#     total = num1 + num2 + num3
#     return total

# num1 = int(input('Please input num1: '))
# num2 = int(input('Please input num2: '))
# num3 = int(input('Please input num3: '))
# print('The total of %d, %d, and %d is %d.' %(num1, num2, num3, sum(num1, num2, num3)))


#homework 2
#make a function which name is max, it return the max value of these three numbers.
#for example:
#print('the max number of %d, %d and %d is %d.' % (a, b, c, max(a, b, c,)))

# def max(num1, num2, num3):
#     # if num1 > num2:
#     #     if num1 > num3:
#     #         return num1
#     #     else:
#     #         return num3
#     # else:
#     #     if num2 > num3:
#     #         return num2 
#     #     else:
#     #         return num3
#     max = num1
#     if max < num2:
#         max = num2
#     if max < num3:
#         max = num3
#     return max
        
# print(max(22, 99, 66))


#make a funcation which name is min, compare 4 numbers and return the smallest number.
# def min(num1, num2, num3, num4):
#     min = num1
#     if min > num2:
#         min = num2
#     if min > num3:
#         min = num3
#     if min > num4:
#         min = num4
#     return min

# print(min(10, 3, 19, 5))


# def min(num1, num2, num3, num4):
#     min = num1 if num1 < num2 else num2
#     min = min if min < num3 else num3
#     min = min if min < num4 else num4

#     return min

# float, int, bool, str, list, dict, tuple, set, frozenset, range, 

# def min(*numbers):
#     min = numbers[1]
#     for number in numbers:
#         if min > number:
#             min = number
#     return min

    # min = num1
    # if min > num2:
    #     min = num2
    # if min > num3:
    #     min = num3
    # if min > num4:
    #     min = num4
    # return min


# def min(*numbers):
#     min = numbers[1]
#     for number in numbers:
#         if min > number:
#             min = number
#     return min

# print(min(10, 3, 5))
# print(min(10, 88, 19, 5))
# print(min(10, 99, 19, 4, 8))
# print(min(10, 2, 19, 5, 9, 66))
# print(min(1, 19))


# def max(*numbers):
#     max = numbers[1]
#     for number in numbers:
#         if max < number:
#             max = number
#     return max

# print(max(40, 3, 5))
# print(max(10, 88, 19, 5))
# print(max(10, 99, 19, 4, 8))
# print(max(10, 2, 19, 5, 9, 66))
# print(max(1, 19))


# # 2, make a function which name is max, it return the max value of these three numbers.
# # e.g.
# # print('the max number of %d, %d and %d is %d.' % (a,b,c,max(a,b,c)))




