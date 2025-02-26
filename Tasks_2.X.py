# lista
my_list = [1, 2, 3]
my_list = list([1, 2, 3])

# krotka
my_tuple = (1, 2, 3)
my_tuple = tuple([1, 2, 3])

# zbiór
my_set = {1, 2, 3}
my_set = set([1, 2, 3])

# słownik
my_dictionary = {
    0: 1,
    1: 2,
    2: 3
}
my_dictionary = dict(((0, 1),(1, 2),(2, 3)))

# wariacja
my_tuple = tuple(my_list)
print(type(my_tuple))

my_list = list(my_tuple)
print(type(my_list))

my_list = list(my_dictionary)
print(type(my_list))
print(my_list)