# table = {}
# for i in range(3):
#     for j in range(3):
#         table[(i,j)] = input('Please input a number: ')
        
# print(table)
# print('tom\tjack')
# for i in range(3):
#     for j in range(3):
#         print(table[(i, j)], '\t', end =' ')
#     print()


# for i in range(3):
#     print(111)


# for j in range(5):
#     print(222)
    

# for i in range(3):
#     print(111)
#     for j in range(5):
#         print(222)

# scores = {}
# scores['tom'] = {}
# scores['tom']['math'] = 99
# scores['tom']['music'] = 90
# scores['tom']['english'] = 95
    
# scores['eric'] = {}
# scores['eric']['math'] = 99
# scores['eric']['music'] = 90
# scores['eric']['english'] = 80

# print(scores)


# myscores = {}
# myscores[('tom', 'math')] = 90
# myscores[('tom', 'music')] = 90
# myscores[('tom', 'english')] = 99

# myscores[('eric', 'math')] = 99
# myscores[('eric', 'music')] = 70
# myscores[('eric', 'english')] = 80

# print(myscores)

# #please input the number of students: 3
# #please input No.1 student name:
# #please input the score of No.1 student math:
# #please input the score of No.1 student music:
# #please input the score of No.1 student english:

# scores = {}
# numbers = int(input('please input the number of students: '))
# for i in range(numbers):
#     name = input('No.%d student name:' % int(i+1))
#     scores[(name, 'math')] = float(input('No.%d student math score:' % int(i+1)))
#     scores[(name, 'music')] = float(input('No.%d student music score:' % int(i+1)))
#     scores[(name, 'english')] = float(input('No.%d student english score:' % int(i+1)))

# print(scores)


# scores = {}
# scores['tom'] = {}
# scores['tom']['math'] = 99
# scores['tom']['music'] = 90
# scores['tom']['english'] = 90


# scores['eric'] = {}
# scores['eric']['math'] = 99
# scores['eric']['music'] = 90
# scores['eric']['english'] = 90

# print(scores)


# template = 'My name: %(name)s, my age: %(age)d, my email: %(email)s'
# course = {
#     'name':'Tom', 
#     'age': 13, 
#     'email': 'teat@gmail.com'
# }

# print(template % course)

# course = {'name':'Jack', 'age': 20, 'email': 'jack@gmail.com'}
# print(template % course)


# mydic = {
#     'name':'Tom', 
#     'age': 13, 
#     'email': 'teat@gmail.com'
# }
# print(type(mydic))
# print(mydic)

# myset = {"1", "22", "333", "22"}
# print(type(myset))
# print(myset)

# mylist = ["1", "2", "3", "2"]
# print(type(mylist))
# print(mylist)


# myset = {
#     1,
#     2,
#     1,
#     (1,2,3),
#     'c',
#     'c'
# }
# print(myset)
# # {
# #     1, 
# #     2, 
# #     'c', 
# #     (1, 2, 3)
# # }


# set1 = set("01234567890123456789")
# set2 = set([1,2,3,4,5,1,2,3,4,5])
# set3 = set((1,2,3,4,5,6,5,4,3,2,1))
# print("set1:", set1)
# print("set2:", set2)
# print("set3:", set3)


# myset = {1,'c',1,(1,2,3),'c'}
# for ele in myset:
#     print(ele, end = ' ')
# print()


# a = {1,'c',1,(1,2,3),'c'}
# print(a)
# del(a)
# print(a)


# scores = {}
# scores['tom'] = {}
# scores['tom']['math'] = 99
# scores['tom']['music'] = 90
# scores['tom']['english'] = 90


# scores['eric'] = {}
# scores['eric']['math'] = 99
# scores['eric']['music'] = 90
# scores['eric']['english'] = 90

# print(scores)

# {
# 'tom': {
# 'math': 99, 
# 'music': 90, 
# 'english': 90
# }, 
# 'eric': {
# 'math': 99, 
# 'music': 90, 
# 'english': 90
# }
# }


# scores = {}
# numbers = int(input('please input the number of students: '))
# for i in range(numbers):
# name = input('No.%d student name:' % int(i+1))
# scores[(name, 'math')] = float(input('No.%d student math score:' % int(i+1)))
# scores[(name, 'music')] = float(input('No.%d student music score:' % int(i+1)))
# scores[(name, 'english')] = float(input('No.%d student english score:' % int(i+1)))


students = {}
number = int(input('Please input the number of students: '))
for a in range(number):
    name = input('Please input the student name: ')
    students[name] = {}
    students[name]['age'] = input('Please input your age: ')
    students[name]['phone'] = input('Please input your phone number: ')
    students[name]['email'] = input('Please input your email: ')
    
print(students)

