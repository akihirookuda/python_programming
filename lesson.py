# import math
#
# num: int = 1
# name: str = '1'
#
# new_num = int(name)
#
# print(new_num, type(new_num))
#
# print('Hi', 'Mike', sep=',', end=',\n')
# print('Hi', 'Mike', sep=',', end='\n')
#
# print(2+2)
#
# result = math.sqrt(25)
# print(result)
#
# y = math.log2(10)
#
# print(y)
#
# print('hello')
# print("hello")
# print("I don't know")
# print('I don\'t know')
# print('say "I don\'t know"')
# print("say \"I don't know\"")
#
# print('hello.\nHow are you?')
# print(r'C:\name\name')
#
# print('#######')
# print("""\
# line1
# line2
# line3\
# """)
# print('#######')
#
# print('Hi.' * 3 + 'Mike.')
# s = ('aaaaaaaaaaaaaaaaaaaaa\nbbbbbbbbbbbbbb')
# print(s)
#
# word = 'python'
# print(word[0])
# print(word[1])
# print(word[-1])
# print(word[0:2])
# print(word[2:5])
# print('##################')
# print(word[0:2])
# print(word[:2])
# print('##################')
# print(word[2:])
# print('##################')
# word = 'j' + word[1:]
# print(word)
# print(word[:])
#
# n = len(word)
# print(n)
# print('##################')
# s = 'My name is Mike. Hi Mike.'
# print(s)
# is_start = s.startswith('My')
# print(is_start)
# is_start = s.startswith('X')
# print(is_start)
#
# print('##################')
# print(s.find('Mike'))
# print(s.rfind('Mike'))
# print(s.count('Mike'))
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.replace('Mike', 'Nancy'))
#
# print('##################')
# r = [1, 2, 3, 4, 5, 1, 2, 3]
# print(r.index(3))
# print(r.index(3, 3))
# print(r.index(2, 5))
# print(r.index(5, 2))
#
# print(r.count(3))
#
# if 1 in r:
#     print('exist')
#
# r.sort()
# print(r)
#
# r.sort(reverse=True)
# print(r)
# r.reverse()
# print(r)
#
# s = 'My name is Mike.'
# to_split = s.split(' ')
# print(to_split)
#
# x = ' ##### '.join(to_split)
# print(x)
#
# i = [1, 2, 3, 4, 5]
# j = i
# j[0] = 100
# print('j=', j)
# print('i=', i)
#
# x = [1, 2, 3, 4, 5]
# y = x[:]
# #y = x.copy()
# y[0] = 100
# print('y=', y)
# print('x=', x)
#
# X = 20
# Y = X
# Y = 5
# print(id(Y))
# print(id(X))
# print(Y)
# print(X)
#
# X = ['a','b']
# Y = X
# Y[0] = 'p'
# print(id(Y))
# print(id(X))
# print(Y)
# print(X)
#
# num_tuple = (10, 20)
#
# print(num_tuple)
#
# x, y = num_tuple
# print(x, y)
#
# x, y = 10, 20
# print(x, y)
#
# min, max = 0, 100
# print(min, max)
#
# i = 10
# j = 20
#
# tmp = i
# i = j
# j = tmp
# print(i,j)
#
# a = 100
# b = 200
# print(a, b)
# a, b = b, a
# print(a, b)
#
# chose_from_two =('A', 'B', 'C')
# #chose_from_two =['A', 'B', 'C']
#
# answer = []
# answer.append('A')
# answer.append('C')
#
# print(chose_from_two)
# print(answer)
# print('##############')
# x = {'a': 1}
# y = x
# y['a'] = 1000
# print(x)
# print(y)
#
# x = {'a': 1}
# y = x.copy()
# y['a'] = 1000
# print(x)
# print(y)
# print('##############')
# fruits = {
#     'apple': 100,
#     'banana': 200,
#     'orange': 300,
#
# }
# print(fruits['apple'])
#
# my_friends = {'a', 'c', 'd'}
# A_friends = {'b','d','e','f'}
#
# print(my_friends & A_friends)
#
# f = {'apple','banana','apple','banana'}
# kind = set(f)
# print(kind)
#
# print('##############')
# print('xxxxxx')
#
# #test
# """
# test
# """
#
# print('xxxxxx')
#
# #Apple price
# some_value = 100
#
# s = 'aaaaaaaaaaaaa'\
#     +'bbbbbbbbbbbbbb'
#
# print(s)
#
# x = 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+\
#     1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1+ 1
#
# print(x)
#
# print('##############')
#
# x = 0
#
# if x < 0:
#     print('negative')
# elif x == 0:
#     print('zero')
# else:
#     print('positive')
#
# a = 5
# b = 10
#
# if a> 0 :
#     print('a is positive')
#     if b> 0:
#         print('b is positive')
#
#
#
# print('##############')
#
# y = [1 , 2 , 3]
# x = 1
# if x in y:
#     print('in')
#
# if 100 not in y:
#     print('not in')
#
# print('##############')
#
# # a = 1
# # b = 2
# #
# # if not a == b:
# #     print('Not equal')
# #
# # if a != b:
# #     print('Not equal')
#
# is_ok = True
#
# if not is_ok:
#     print('hello')
#
# #is_ok = True
# is_ok = [1,2,3,4]
#
# if is_ok:
#     print('OK!')
# else:
#     print('No!')
#
# print('##############')
#
# is_empty = None
# # print(help(is_empty))
#
# if is_empty is None:
#     print('None!!!')
#
# print(1 == True)
# print(1 is True)
# print(None is None)
#
#
# count = 0
# # while count < 5:
# #     print(count)
# #     count +=1
#
# count = 0
# while True:
#     if count >= 5:
#         break
#     print(count)
#     count += 1
#
#     if count == 2:
#         count += 1
#         continue
#     print(count)
#  #   count += 1
#
# count = 0
#
# while count < 5:
#     if count == 1:
#         break
#     print(count)
#     count += 1
# else:
#     print('done')
#
# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

# some_list = [1,2,3,4,5]

print('##################')


# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:
#     print(i)
#
# for s in 'abcdef':
#     print(s)

# for word in ['My','name','is','Mike.']:
#     if word == 'name':
#         continue
# #     print(word)
#
# for fruit in ['apple','banana','orange']:
#     if fruit == 'banana':
#         print('stop eating')
#         break
#     print(fruit)
# else:
#     print('I ate all')

# num_list=[0,1,2,3,4,5,6,7,8,9]
#
# for i in range(2,10,3):
#     print(i)
#
# for i in range(10):
#     print(i,'Hello')
#
# for _ in range(10):
#     print('hello')

# i = 0
# for i, fruit in enumerate(['apple','banana','orange']):
#     print(i, fruit)
#
# days = ['Mon','Tue', 'Wed']
# fruits = ['apple','banana','orange']
# drinks =['coffee','tea','beer']
#
# for i in range(len(days)):
#     print(days[i], fruits[i],drinks[i])
# print('##################')
# for day,fruit,drink in zip(days,fruits,drinks):
#     print(day,fruit,drink)
#
# d = {'x': 100, 'y': 200}
#
# print(d.items())
# for k, v in d.items():
#     print(k, ':', v)

# def say_something():
#     s = 'hi'
#     return s
#
# result = say_something()
# print(result)
#
# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     elif color == 'green':
#         return 'green pepper'
#     else:
#         return "i don't know"
#
# result = what_is_this('red')
# result = what_is_this('green')
# print(result)

# def add_num(a:int , b:int)->int:
#     return a + b
#
# r = add_num('a' , 'b')
# print(r)
#
# def menu(entree = 'beef', drink = 'wine', dessert= 'ice'):
#     print('entree=',entree)
#     print('drink=',drink)
#     print('dessert=',dessert)
#
#
# menu(entree = 'chicken', drink= 'beer')
#
# def test_func(x , l = None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l

# y = [1,2,3]
# r = test_func(100,y)
# print(r)
#
# y = [1,2,3]
# r = test_func(200, y)
# print(r)

# r = test_func(100)
# print(r)
#
# r = test_func(100)
# print(r)
#
# def say_something(word, *args):
#     print('word= ',word)
#     for arg in args:
#         print(arg)
#
# # say_something('Hi', 'Mike', 'Nance')
#
# #t = ('Mike', 'Nancy')
# #say_something('Hi', *t)

# def menu(food, *args, **kwargs):
#     # print(kwargs)
#         print(food)
#         print(args)
#         print(kwargs)
#
# # menu(entree='beef', drink='coffee')
#
# # d = {
# #     'entree': 'beef',
# #     'drink': 'ice coffee',
# #     'dessert': 'ice'
# # }
#
# menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

#

# def outer(a, b):
#
#     def plus(c, d):
#         return c + d
#
#     r1 = plus(a, b)
#     r2 = plus(b, a)
#     print(r1 + r2)
#
# outer(1, 2)

# def outer(a,b):
#
#     def inner():
#         return a + b
#
#     return inner
#
# f = outer(1,2)
# r= f()
# print(r)

# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius
#
#     return circle_area
#
# ca1 = circle_area_func(3.14)
# ca2 = circle_area_func(3.141592)
#
# print(ca1(10))
# print(ca2(10))

# def print_more(func):
#     def warpperi(*args,**kwargs):
#         print('func:', func.__name__)
#         print('args:',args)
#         print('kwargs:',kwargs)
#         result = func(*args, **kwargs)
#         print('result:',result)
#         return result
#     return warpperi
#
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func (*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
#
# @print_info
# @print_more
# def add_num(a, b):
#     return a + b
#
# r = add_num(10,20)
# print(r)

# @print_info
# def sub_num(a, b):
#     return a - b

# r = sub_num(10,20)
# print(r)


# f= print_inf(add_num)
# r= f(10,20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')
#
# print(r)

# l = ['Mon','tue', 'Wed','Thu','fri','sat','Sun']
#
# def chang_words(words, func):
#     for word in words:
#         print(func(word))
#
# def sample_func(word):
#     return word.capitalize
#
# def sample_func2(word):
#     return word.lower()
#
# # sample_func = lambda word: word.capitalize()
#
# chang_words(l, lambda word: word.capitalize())
#
# chang_words(l, lambda word: word.lower())

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('###############')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)

g = greeting()
print(next(g))
