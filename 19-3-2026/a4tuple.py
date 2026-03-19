#wht will be the output of the following code block?

init_tuple = ()
print(init_tuple.__len__())


init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print(init_tuple_a == init_tuple_b)
#here diff? in tuple its not mandatory to use () but in list it is mandatory to use [] for creating a list. so both are same. but in tuple we can create a tuple without using () but in list we cannot create a list without using [].


init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print(init_tuple_a + init_tuple_b)
#check address of the tuple
print(id(init_tuple_a))
print(id(init_tuple_b))


l = [1,2,3]
init_tuple = ('python',) * (l.__len__() - l [:: -1][0])
print(init_tuple)



init_tuple = ('python') * 3
print(type(init_tuple)) # double, single qoute me string he aata h

init_tuple = ('python',) * 3
print(type(init_tuple))


# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple) # tuple is immutable we cannot change the value of the tuple but we can change the value of the list. so it will give error.
# #TypeError: 'tuple' object does not support item assignment




init_tuple = ((1, 2),)*7
print(len(init_tuple[3:8])) # it will give 7 because we are creating a tuple of 7 elements and each element is a tuple of 2 elements. so it will give 7.
