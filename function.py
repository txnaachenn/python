# def maxEvenNumber(*numbers):
#     maxEven = 3
#     for number in numbers:
#         if number % 2 == 0:
#             maxEven = number
#             break

#     if maxEven == 3:
#         return 'It does not have a even number.'
#     else:
#         return 'It has a even number.'

# # if maxEven < number:
# # maxEven = number
# # return max


# def maxEvenNumber(*numbers):
#     lstEven= []
#     for number in numbers:
#         if number % 2 == 0:
#             lstEven.append(number)

#     if len(lstEven) == 0:
#         return None
#     else:
#         max = lstEven[0]
#         for value in lstEven:
#             if max < value:
#                 max = value
#         return max

# print(maxEvenNumber(1,3,6,8,9,0,99,66,44,88,77))
# print(maxEvenNumber(33,11,51,89,93,31,13,55,31))
# print(maxEvenNumber(9,11,4,77,3,67,35,23,25,47))


# def min(a, b):
#     if a < b:
#         return a
#     else:
#         return b
    
# print(min(34, 56))
# print(min(10, 5))
# print(min(1, 64))
# print(min(29, 38))


# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# print(max(34, 56))
# print(max(10, 5))
# print(max(1, 64))
# print(max(29, 38))


# str = 'abcdefg'

# for  char in str:
#     print(char)


# str = input('Please input a string: ')

# n = 0
# for char in str:
#     n = n + 1

# print(n)


# def my_len(myString):
#     n = 0
#     for char in myString:
#         n = n + 1
#     return n

# str = input('Please input a string: ')
# print(my_len(str))


def full_name(firstname, middlename, lastname):
    return firstname + ' ' +  middlename  +     ' ' +         lastname


print(full_name('Christina', 'hi', 'Chen'))
print(full_name('Christ', 'yes', 'Ch'))
print(full_name('qqq', 'bye', 'Chen'))

# print('eric' + ' ' + 'Gao')