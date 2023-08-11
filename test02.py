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


# students = {}
# number = int(input('Please input the number of students: '))
# for a in range(number):
#     name = input('Please input the student name: ')
#     students[name] = {}
#     students[name]['age'] = input('Please input your age: ')
#     students[name]['phone'] = input('Please input your phone number: ')
#     students[name]['email'] = input('Please input your email: ')
    
# # print(students)


# print('-----------------------------------------------------------------------')
# print('| %10s | %17s | %17s | %17s |' % ('Name', 'Age', 'Phone', 'Email'))
# print('-----------------------------------------------------------------------')
# for name, student in students.items():
#     print('|%10s ' % name, end = '')
#     for key, value in student.items():    
#         print('|%17s ' % value, end = '')
#         # print(key, value)
#     print('｜')
# print('-----------------------------------------------------------------------')


# set1={1,2,3}
# set2={3,4,5}

# print(set1 & set2) # 集合的交集 {3}
# print(set1 | set2) # 集合的并集 {1, 2, 3, 4, 5}

# print(set1 - set2) # {1, 2}
# print(set2 - set1) # {4, 5}

# print(set1 ^ set2) # 对称差集（非集） {1, 2, 4, 5}


# 全班所有同学都选课了，大家各自都选择了自己的课程。
# 以下的同学选了数学：
# Amy, Tom, Jack, Tim, Kelly, Jacky, Aurora, Hieu
# 以下的同学都选了篮球：
# Jason, Jacky, Tom, Tim, Max, Jack, Rex, Kunal
# 以下的同学都选择了Python编程：
# Christina, Jason, Tim, Hieu, Selina, Jack, Jerry

# 请把以上数据存入三个集合（set），然后通过集合做交集、并集、差集运算，计算出以下数据：
# 1，全班一共有多少同学，每个同学的名字是什么？
# 2，同时选择三门课程的有多少人，都是谁？
# 3，只选择数学的有几人，都是谁？
# 4，都有哪些同学只选择了一门课，都是谁，多少人？

# math = {'Amy', 'Tom', 'Jack', 'Tim', 'Kelly', 'Jacky', 'Aurora', 'Hieu'}
# basketball = {'Jason', 'Jacky', 'Tom', 'Tim', 'Max', 'Jack', 'Rex', 'Kunal'}
# python = {'Christina', 'Jason', 'Tim', 'Hieu', 'Selina', 'Jack', 'Jerry'}

# all = math | basketball | python
# print('There are %d students in the class' % len(all))
# print(all)


# common = math & basketball & python
# print('There are %d students who chose 3 classes' % len(common))
# print(common)


# mathonly = math - basketball - python
# print('There are %d students who chose math only' % len(mathonly))
# print(mathonly)


# basketballonly = basketball - math - python
# print('There are %d student who chose basketball only' % len(basketballonly))
# print(basketballonly)


# pythononly = python - math - basketball
# print('There are %d students who chose python only' % len(pythononly))
# print(pythononly)


# pythononly2 = python - (math | basketball)
# print('There are %d students who chose python only' % len(pythononly2))
# print(pythononly2)


# mathonly2 = math - (basketball | python)
# print('There are %d students who chose math only' % len(mathonly2))
# print(mathonly2)


# unique = math ^ basketball ^ python
# print('There are %d students who chose only one unit' % len(unique))
# print(unique)


# s = {'Python', 'C', 'C++'}
# fs = frozenset(['Java', 'Shell'])
# s_sub = {'PHP', 'C#'}

# s.add(fs)
# print('s =', s)

# s.add(s_sub)
# print('s =', s)

# print(type(s))
# print(type(fs))
# print(type(s_sub))


# print('Hello world')


# for i in range(1, 3):
#     print('%d: Hello world1' % (i))
#     print('%d: Hello world2' % (i))
#     print('%d: Hello world3' % (i))
#     print('%d: Hello world4' % (i))


# name = 'kayley'
# age = 9
# email = 'kayley.chen@student.qmc.school.nz'

# print('%s is a stupid child, age is %d, email is %s.' % (name, age, email))


# aaaa
# {
#     print('%d: Hello world1' % (i))
#     print('%d: Hello rorld2' % (i))
#     print('%d: Hello world3' % (i))
#     print('%d: Hello world4' % (i))
# }


# num1 = int(input('Please input number 1: '))
# num2 = int(input('Please input number 2: '))
# num3 = int(input('Please input number 3: '))

# if num1 > num2:
#     if num1 > num3:
#         print(num1)
#     else:
#         print(num3)
# else:
#     if num2 > num3:
#         print(num2) 
#     else:
#         print(num3)


numbers = (33,44,6,8,66)

min = numbers[0]
for number in numbers:
    if min > number:
        min = number

print(min)
